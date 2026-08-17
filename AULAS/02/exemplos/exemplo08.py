import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout
from PySide6.QtGui import QPalette, QColor
from PySide6.QtCore import QSize

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Aninhando Layouts")
        self.setFixedSize(QSize(400, 300))
        
        layout1 = QHBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QVBoxLayout()
        
        layout1.setContentsMargins(0, 0, 0, 0)
        layout1.setSpacing(10)
        
        layout2.setContentsMargins(0, 20, 50, 20)
        layout2.setSpacing(5)
        layout2.addWidget(Cor("red"))
        layout2.addWidget(Cor("blue"))
        layout2.addWidget(Cor("purple"))
        
        layout1.addLayout(layout2)
        layout1.addWidget(Cor("green"))
        
        layout3.addWidget(Cor("red"))
        layout3.addWidget(Cor("purple"))
        
        layout1.addLayout(layout3)
        
        central_widget = QWidget()
        central_widget.setLayout(layout1)
        
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