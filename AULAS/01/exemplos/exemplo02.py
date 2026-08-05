from PySide6.QtWidgets import QApplication, QPushButton
import sys

app = QApplication(sys.argv)

window = QPushButton("Clique aqui")
window.show()

app.exec()