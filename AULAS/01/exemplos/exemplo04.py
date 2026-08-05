import sys
from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Meu querido aplicativo")
        self.setFixedSize(QSize(400, 300))
        # Descomente as linhas abaixo para permitir redimensionamento da janela
        # self.setMinimumHeight(200)
        # self.setMinimumWidth(300)
        # self.setMaximumHeight(600)
        # self.setMaximumWidth(800)

        button = QPushButton("Clique aqui")
        # Configurando o widget central da janela principal para ser o botão
        self.setCentralWidget(button)
        
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()