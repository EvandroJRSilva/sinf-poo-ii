import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QToolBar

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Barra de Ferramentas")
        
        label = QLabel("Olá!")
        # O namespace `Qt` tem muitos atributos para customizar widgets. 
        # Veja: http://doc.qt.io/qt-6/qt.html
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setCentralWidget(label)

        self.toolbar = QToolBar("Nome da barra de ferramentas")
        self.addToolBar(self.toolbar)
        
        

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()