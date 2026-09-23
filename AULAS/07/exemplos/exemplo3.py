import sys, csv
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QHBoxLayout, QPushButton, QTableWidget, QTableWidgetItem,
    QFileDialog, QMessageBox, QLabel, QAbstractItemView
)
from PySide6.QtCore import Qt


class CsvEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Editor de Arquivo CSV")
        self.setMinimumSize(800, 520)
        self._build_ui()

    def _build_ui(self):
        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)
        layout.setSpacing(8)
        layout.setContentsMargins(12, 12, 12, 12)

        self.label = QLabel("Nenhum arquivo CSV carregado.")
        self.label.setStyleSheet("color: gray; font-size: 12px;")
        layout.addWidget(self.label)

        self.table = QTableWidget()
        self.table.setAlternatingRowColors(True)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        layout.addWidget(self.table)

        btn_layout = QHBoxLayout()
        for text, slot in [
            ("📂 Abrir CSV", self.open_csv),
            ("💾 Salvar CSV", self.save_csv),
            ("➕ Linha", self.add_row),
            ("➕ Coluna", self.add_column),
            ("❌ Remover Linha", self.remove_row),
        ]:
            btn = QPushButton(text)
            btn.clicked.connect(slot)
            btn_layout.addWidget(btn)

        layout.addLayout(btn_layout)

    # ── ações ─────────────────────────────────────────────────────────────────
    def open_csv(self):
        path, _ = QFileDialog.getOpenFileName(
            self, "Abrir CSV", "", "Arquivos CSV (*.csv);;Todos (*)"
        )
        if not path:
            return
        try:
            with open(path, newline="", encoding="utf-8") as f:
                reader = csv.reader(f)
                rows = list(reader)

            if not rows:
                QMessageBox.warning(self, "Aviso", "O arquivo está vazio.")
                return

            headers, *data_rows = rows
            self.table.setColumnCount(len(headers))
            self.table.setRowCount(len(data_rows))
            self.table.setHorizontalHeaderLabels(headers)

            for r, row in enumerate(data_rows):
                for c, cell in enumerate(row):
                    self.table.setItem(r, c, QTableWidgetItem(cell))

            self.table.resizeColumnsToContents()
            self.label.setText(f"Arquivo: {path}  |  {len(data_rows)} linhas × {len(headers)} colunas")
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Não foi possível abrir:\n{e}")

    def save_csv(self):
        path, _ = QFileDialog.getSaveFileName(
            self, "Salvar CSV", "", "Arquivos CSV (*.csv)"
        )
        if not path:
            return
        try:
            with open(path, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                # cabeçalho
                headers = [
                    self.table.horizontalHeaderItem(c).text()
                    for c in range(self.table.columnCount())
                ]
                writer.writerow(headers)
                # dados
                for r in range(self.table.rowCount()):
                    row = []
                    for c in range(self.table.columnCount()):
                        item = self.table.item(r, c)
                        row.append(item.text() if item else "")
                    writer.writerow(row)
            QMessageBox.information(self, "Sucesso", "CSV salvo com sucesso!")
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Não foi possível salvar:\n{e}")

    def add_row(self):
        row = self.table.rowCount()
        self.table.insertRow(row)
        for c in range(self.table.columnCount()):
            self.table.setItem(row, c, QTableWidgetItem(""))

    def add_column(self):
        col = self.table.columnCount()
        self.table.insertColumn(col)
        self.table.setHorizontalHeaderItem(col, QTableWidgetItem(f"Coluna {col + 1}"))

    def remove_row(self):
        rows = sorted({idx.row() for idx in self.table.selectedIndexes()}, reverse=True)
        for r in rows:
            self.table.removeRow(r)
        if not rows:
            QMessageBox.information(self, "Aviso", "Selecione ao menos uma linha para remover.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CsvEditor()
    window.show()
    sys.exit(app.exec())