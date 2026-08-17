import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from PySide6.QtGui import QPalette, QColor
from PySide6.QtCore import QSize

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("QVBoxLayout")
        self.setFixedSize(QSize(400, 300))
        
        layout = QVBoxLayout()
        layout.addWidget(Cor("red"))
        layout.addWidget(Cor("green"))
        layout.addWidget(Cor("blue"))
        layout.addWidget(Cor("yellow"))
        
        central_widget = QWidget()
        central_widget.setLayout(layout)
        
        self.setCentralWidget(central_widget)

# Para facilitar a visualização dos layouts vamos criar um widget para mostrar cores que escolhermos
class Cor(QWidget):
    def __init__(self, cor):
        super().__init__()
        
        self.setAutoFillBackground(True)
        
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(cor))
        self.setPalette(palette)


app = QApplication(sys.argv)
    
window = MainWindow()
window.show()

app.exec()