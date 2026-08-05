import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Meu querido primeiro aplicativo")

        button = QPushButton("Clique aqui")
        # Configurando o widget central da janela principal para ser o botão
        self.setCentralWidget(button)
        
app = QApplication(sys.argv)
    
window = MainWindow()
window.show()

app.exec()