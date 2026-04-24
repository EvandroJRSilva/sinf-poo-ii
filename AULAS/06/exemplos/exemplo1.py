import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QHBoxLayout, QPushButton, QTextEdit, QLabel,
    QFileDialog, QMessageBox, QStatusBar
)
from PySide6.QtCore import Qt


class TextFileEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Editor de Arquivo de Texto")
        self.setMinimumSize(700, 500)
        self.current_file = None
        self._build_ui()

    def _build_ui(self):
        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)
        layout.setSpacing(8)
        layout.setContentsMargins(12, 12, 12, 12)

        self.label = QLabel("Nenhum arquivo aberto")
        self.label.setStyleSheet("color: gray; font-size: 12px;")
        layout.addWidget(self.label)

        self.text_edit = QTextEdit()
        self.text_edit.setPlaceholderText("O conteúdo do arquivo aparecerá aqui...")
        layout.addWidget(self.text_edit)

        btn_layout = QHBoxLayout()
        for text, slot in [
            ("📂 Abrir", self.open_file),
            ("💾 Salvar", self.save_file),
            ("💾 Salvar Como", self.save_file_as),
            ("🗑️ Limpar", self.text_edit.clear),
        ]:
            btn = QPushButton(text)
            btn.clicked.connect(slot)
            btn_layout.addWidget(btn)

        layout.addLayout(btn_layout)
        self.setStatusBar(QStatusBar())

    def open_file(self):
        path, _ = QFileDialog.getOpenFileName(
            self, "Abrir Arquivo", "", "Arquivos de Texto (*.txt);;Todos (*)"
        )
        if path:
            try:
                with open(path, "r", encoding="utf-8") as f:
                    self.text_edit.setPlainText(f.read())
                self.current_file = path
                self.label.setText(f"Arquivo: {path}")
                self.statusBar().showMessage("Arquivo aberto com sucesso.", 3000)
            except Exception as e:
                QMessageBox.critical(self, "Erro", f"Não foi possível abrir:\n{e}")

    def save_file(self):
        if self.current_file:
            self._write(self.current_file)
        else:
            self.save_file_as()

    def save_file_as(self):
        path, _ = QFileDialog.getSaveFileName(
            self, "Salvar Como", "", "Arquivos de Texto (*.txt);;Todos (*)"
        )
        if path:
            self._write(path)
            self.current_file = path
            self.label.setText(f"Arquivo: {path}")

    def _write(self, path):
        try:
            with open(path, "w", encoding="utf-8") as f:
                f.write(self.text_edit.toPlainText())
            self.statusBar().showMessage("Arquivo salvo com sucesso.", 3000)
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Não foi possível salvar:\n{e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TextFileEditor()
    window.show()
    sys.exit(app.exec())