import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Meu Aplicativo de Evento")
        self.setFixedWidth(600)
        self.setMouseTracking(True) # Habilita o rastreamento do mouse mesmo sem clicar
        
        self.label = QLabel("Clique nessa janela")
        
        # É necessário habilitar o rastreamento do mouse para o label também, caso contrário, 
        # os eventos de mouse só serão capturados quando o mouse estiver sobre a janela, mas não sobre o label.
        self.label.setMouseTracking(True) # Habilita o rastreamento do mouse mesmo sem clicar
        
        self.setCentralWidget(self.label)
        
    def mouseMoveEvent(self, event):
        self.label.setText("mouseMoveEvent")
    
    def mousePressEvent(self, event): 
        self.label.setText("mousePressEvent")
    
    def mouseReleaseEvent(self, event):
        self.label.setText("mouseReleaseEvent")
    
    def mouseDoubleClickEvent(self, event):
        self.label.setText("mouseDoubleClickEvent")
        
app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()