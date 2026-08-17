import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QHBoxLayout
from PySide6.QtGui import QPalette, QColor
from PySide6.QtCore import QSize

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("QGridLayout")
        self.setFixedSize(QSize(400, 300))
        
        layout = QGridLayout()
        layout2 = QHBoxLayout()
        
        layout2.addWidget(Cor("darkBlue"))
        layout2.addWidget(Cor("gray"))

        layout.addWidget(Cor('red'), 0, 0)
        layout.addWidget(Cor('green'), 1, 0)
        layout.addWidget(Cor('blue'), 1, 1)
        layout.addWidget(Cor('purple'), 3, 2)
        
        layout.addLayout(layout2, 2, 0, 3, 2)
        
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