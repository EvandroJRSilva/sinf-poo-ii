import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Meu Aplicativo de MouseEvent")
        self.setFixedWidth(400)
        
        self.label = QLabel("Clique nessa janela")
        self.setCentralWidget(self.label)
        
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.label.setText("Botão esquerdo do mouse pressionado!")
        elif event.button() == Qt.MouseButton.RightButton:
            self.label.setText("Botão direito do mouse pressionado!")
        elif event.button() == Qt.MouseButton.MiddleButton:
            self.label.setText("Botão do meio do mouse pressionado!")
            
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.label.setText("Botão esquerdo do mouse liberado!")
        elif event.button() == Qt.MouseButton.RightButton:
            self.label.setText("Botão direito do mouse liberado!")
        elif event.button() == Qt.MouseButton.MiddleButton:
            self.label.setText("Botão do meio do mouse liberado!")
            
    def mouseDoubleClickEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.label.setText("Botão esquerdo do mouse duplamente clicado!")
        elif event.button() == Qt.MouseButton.RightButton:
            self.label.setText("Botão direito do mouse duplamente clicado!")
        elif event.button() == Qt.MouseButton.MiddleButton:
            self.label.setText("Botão do meio do mouse duplamente clicado!")
            
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()