import sys, json
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QHBoxLayout, QPushButton, QTreeWidget, QTreeWidgetItem,
    QFileDialog, QMessageBox, QLabel
)
from PySide6.QtCore import Qt


class JsonViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Visualizador / Editor de JSON")
        self.setMinimumSize(750, 550)
        self.data = {}
        self._build_ui()

    def _build_ui(self):
        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)
        layout.setSpacing(8)
        layout.setContentsMargins(12, 12, 12, 12)

        self.label = QLabel("Nenhum arquivo JSON carregado.")
        self.label.setStyleSheet("color: gray; font-size: 12px;")
        layout.addWidget(self.label)

        self.tree = QTreeWidget()
        self.tree.setHeaderLabels(["Chave", "Valor"])
        self.tree.setColumnWidth(0, 250)
        layout.addWidget(self.tree)

        btn_layout = QHBoxLayout()
        for text, slot in [
            ("📂 Abrir JSON", self.open_json),
            ("💾 Salvar JSON", self.save_json),
            ("➕ Adicionar Item", self.add_item),
            ("❌ Remover Item", self.remove_item),
        ]:
            btn = QPushButton(text)
            btn.clicked.connect(slot)
            btn_layout.addWidget(btn)

        layout.addLayout(btn_layout)

    # ── helpers ──────────────────────────────────────────────────────────────
    def _populate_tree(self, data, parent=None):
        """Constrói a árvore recursivamente a partir de qualquer JSON."""
        root = parent or self.tree.invisibleRootItem()
        if isinstance(data, dict):
            for k, v in data.items():
                item = QTreeWidgetItem(root, [str(k), "" if isinstance(v, (dict, list)) else str(v)])
                item.setFlags(item.flags() | Qt.ItemIsEditable)
                self._populate_tree(v, item)
        elif isinstance(data, list):
            for i, v in enumerate(data):
                item = QTreeWidgetItem(root, [f"[{i}]", "" if isinstance(v, (dict, list)) else str(v)])
                item.setFlags(item.flags() | Qt.ItemIsEditable)
                self._populate_tree(v, item)

    def _tree_to_dict(self, parent=None):
        """Reconstrói o dicionário Python a partir da árvore editável."""
        root = parent or self.tree.invisibleRootItem()
        result = {}
        for i in range(root.childCount()):
            item = root.child(i)
            key = item.text(0)
            if item.childCount():
                result[key] = self._tree_to_dict(item)
            else:
                result[key] = item.text(1)
        return result

    # ── ações ─────────────────────────────────────────────────────────────────
    def open_json(self):
        path, _ = QFileDialog.getOpenFileName(
            self, "Abrir JSON", "", "Arquivos JSON (*.json);;Todos (*)"
        )
        if path:
            try:
                with open(path, "r", encoding="utf-8") as f:
                    self.data = json.load(f)
                self.tree.clear()
                self._populate_tree(self.data)
                self.tree.expandAll()
                self.label.setText(f"Arquivo: {path}")
                self.current_file = path
            except Exception as e:
                QMessageBox.critical(self, "Erro", f"JSON inválido ou ilegível:\n{e}")

    def save_json(self):
        path, _ = QFileDialog.getSaveFileName(
            self, "Salvar JSON", "", "Arquivos JSON (*.json)"
        )
        if path:
            try:
                with open(path, "w", encoding="utf-8") as f:
                    json.dump(self._tree_to_dict(), f, ensure_ascii=False, indent=2)
                QMessageBox.information(self, "Sucesso", "JSON salvo com sucesso!")
            except Exception as e:
                QMessageBox.critical(self, "Erro", f"Não foi possível salvar:\n{e}")

    def add_item(self):
        item = QTreeWidgetItem(self.tree, ["nova_chave", "novo_valor"])
        item.setFlags(item.flags() | Qt.ItemIsEditable)
        self.tree.setCurrentItem(item)
        self.tree.editItem(item, 0)

    def remove_item(self):
        for item in self.tree.selectedItems():
            (item.parent() or self.tree.invisibleRootItem()).removeChild(item)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = JsonViewer()
    window.show()
    sys.exit(app.exec())