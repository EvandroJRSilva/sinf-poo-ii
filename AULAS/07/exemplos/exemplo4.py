import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout,
    QHBoxLayout, QPushButton, QTextEdit, QFileDialog, QMessageBox
)
from PySide6.QtCore import (
    QFile, QIODevice, QTextStream, QStringConverter,
    QJsonDocument, QJsonParseError
)


# ──────────────────────────────────────────────────────────────────────────────
# Aba 1 — Texto  (QFile + QTextStream)
# ──────────────────────────────────────────────────────────────────────────────
class TextTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

        self.editor = QTextEdit(placeholderText="Conteúdo do arquivo…")
        layout.addWidget(self.editor)

        bar = QHBoxLayout()
        for label, slot in [("Abrir", self.abrir), ("Salvar", self.salvar)]:
            btn = QPushButton(label)
            btn.clicked.connect(slot)
            bar.addWidget(btn)
        layout.addLayout(bar)

    def abrir(self):
        path, _ = QFileDialog.getOpenFileName(self, "Abrir", "", "Texto (*.txt)")
        if not path:
            return

        arquivo = QFile(path)
        if not arquivo.open(QIODevice.OpenModeFlag.ReadOnly | QIODevice.OpenModeFlag.Text):
            QMessageBox.critical(self, "Erro", arquivo.errorString())
            return

        stream = QTextStream(arquivo)
        stream.setEncoding(QStringConverter.Encoding.Utf8)
        self.editor.setPlainText(stream.readAll())   # lê tudo de uma vez
        arquivo.close()

    def salvar(self):
        path, _ = QFileDialog.getSaveFileName(self, "Salvar", "", "Texto (*.txt)")
        if not path:
            return

        arquivo = QFile(path)
        if not arquivo.open(QIODevice.OpenModeFlag.WriteOnly | QIODevice.OpenModeFlag.Text):
            QMessageBox.critical(self, "Erro", arquivo.errorString())
            return

        stream = QTextStream(arquivo)
        stream.setEncoding(QStringConverter.Encoding.Utf8)
        stream << self.editor.toPlainText()          # escreve com o operador 
        arquivo.close()


# ──────────────────────────────────────────────────────────────────────────────
# Aba 2 — JSON  (QFile + QJsonDocument)
# ──────────────────────────────────────────────────────────────────────────────
class JsonTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

        self.editor = QTextEdit(placeholderText="Conteúdo JSON…")
        layout.addWidget(self.editor)

        bar = QHBoxLayout()
        for label, slot in [("Abrir", self.abrir), ("Salvar", self.salvar)]:
            btn = QPushButton(label)
            btn.clicked.connect(slot)
            bar.addWidget(btn)
        layout.addLayout(bar)

    def abrir(self):
        path, _ = QFileDialog.getOpenFileName(self, "Abrir", "", "JSON (*.json)")
        if not path:
            return

        # 1. Lê os bytes brutos com QFile
        arquivo = QFile(path)
        if not arquivo.open(QIODevice.OpenModeFlag.ReadOnly):
            QMessageBox.critical(self, "Erro", arquivo.errorString())
            return
        bytes_raw = arquivo.readAll()   # retorna QByteArray
        arquivo.close()

        # 2. Valida e analisa com QJsonDocument
        erro = QJsonParseError()
        doc = QJsonDocument.fromJson(bytes_raw, erro)

        if erro.error != QJsonParseError.ParseError.NoError:
            QMessageBox.critical(self, "JSON inválido", erro.errorString())
            return

        # 3. Exibe o JSON indentado no editor
        self.editor.setPlainText(
            doc.toJson(QJsonDocument.JsonFormat.Indented).toStdString()
        )

    def salvar(self):
        path, _ = QFileDialog.getSaveFileName(self, "Salvar", "", "JSON (*.json)")
        if not path:
            return

        # 1. Valida o texto atual antes de salvar
        texto = self.editor.toPlainText().encode("utf-8")
        erro = QJsonParseError()
        doc = QJsonDocument.fromJson(texto, erro)

        if erro.error != QJsonParseError.ParseError.NoError:
            QMessageBox.critical(self, "JSON inválido", erro.errorString())
            return

        # 2. Grava os bytes com QFile
        arquivo = QFile(path)
        if not arquivo.open(QIODevice.OpenModeFlag.WriteOnly):
            QMessageBox.critical(self, "Erro", arquivo.errorString())
            return

        arquivo.write(doc.toJson(QJsonDocument.JsonFormat.Indented))
        arquivo.close()


# ──────────────────────────────────────────────────────────────────────────────
# Janela principal
# ──────────────────────────────────────────────────────────────────────────────
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QFile · QTextStream · QJsonDocument")
        self.setMinimumSize(600, 400)

        abas = QTabWidget()
        abas.addTab(TextTab(), "Texto  (QFile + QTextStream)")
        abas.addTab(JsonTab(), "JSON   (QFile + QJsonDocument)")
        self.setCentralWidget(abas)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = MainWindow()
    janela.show()
    sys.exit(app.exec())