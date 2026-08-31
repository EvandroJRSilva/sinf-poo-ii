import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Message Box")
        self.setMinimumWidth(300)
        self.setMinimumHeight(200)
        
        botao = QPushButton("Clique aqui para aparecer um Message Box")
        botao.clicked.connect(self.botao_clicado)
        self.setCentralWidget(botao)
        
    def botao_clicado(self, s):
        # FORMA 1
        message_box = QMessageBox(self) # passando a MainWindow como parent
        message_box.setWindowTitle("Eu tenho uma pergunta")
        message_box.setText("Você está estudando?")
        message_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        botao = message_box.exec()
        
        # FORMA 2 - utilizando as funções estáticas
        # botao = QMessageBox.question(self, "Eu tenho uma pergunta", "Você está estudando?")
        #
        if botao == QMessageBox.StandardButton.Yes:
            print("SIM!")
        else:
            print("NÃO!")
            
app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()