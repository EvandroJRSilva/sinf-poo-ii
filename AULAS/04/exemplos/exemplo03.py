import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel

class OutraJanela(QWidget):
    """
    Widget genérico, sem pai, portanto, é uma janela
    """
    
    def __init__(self, texto):
        super().__init__()
        
        layout = QVBoxLayout()
        self.label = QLabel(texto)
        layout.addWidget(self.label)
        self.setLayout(layout)
        
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Instanciando aqui
        # ----------------------------------------------------------------
        self.nova_janela1 = OutraJanela("Janela 1")
        self.nova_janela2 = OutraJanela("Janela 2")
        # ----------------------------------------------------------------
        
        layout = QVBoxLayout()
        
        botao1 = QPushButton("Clique aqui para abrir a janela 1")
        botao1.clicked.connect(self.mostrar_janela1)
        # botao1.clicked.connect(lambda checked: self.mostrar_janela(self.nova_janela1))
        layout.addWidget(botao1)
        
        botao2 = QPushButton("Clique aqui para abrir a janela 2")
        botao2.clicked.connect(self.mostrar_janela2)
        # botao2.clicked.connect(lambda checked: self.mostrar_janela(self.nova_janela2))
        layout.addWidget(botao2)
        
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
    
    def mostrar_janela1(self):
        if self.nova_janela1.isVisible():
            self.nova_janela1.hide()
        else:
            self.nova_janela1.show()
        
        
    def mostrar_janela2(self):
        if self.nova_janela2.isVisible():
            self.nova_janela2.hide()
        else:
            self.nova_janela2.show()
            
    def mostrar_janela(self, janela):
        if janela.isVisible():
            janela.hide()
        else:
            janela.show()
        
app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()