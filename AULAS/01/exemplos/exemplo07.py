import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Meu Lindo Aplicativo")
        self.setFixedWidth(600)
        
        self.label = QLabel()
        
        self.input = QLineEdit()
        self.input.textChanged.connect(self.label.setText)
        
        layout = QVBoxLayout() # Vamos ver sobre layout em outra aula
        layout.addWidget(self.input)
        layout.addWidget(self.label)
        
        containter = QWidget()
        containter.setLayout(layout)
        
        self.setCentralWidget(containter)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()