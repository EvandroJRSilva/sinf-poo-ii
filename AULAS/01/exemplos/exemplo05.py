import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Meu Aplicativo Querido")

        button = QPushButton("Clique Aqui!")
        button.setCheckable(True)
        button.clicked.connect(self.botao_clicado)
        button.clicked.connect(self.botao_ligado)

        # Configurando o widget central da janela principal para ser o botão
        self.setCentralWidget(button)

    def botao_clicado(self):
        print("Botão clicado!")

    def botao_ligado(self, estado):
        if estado:
            print("Botão ligado!")
        else:
            print("Botão desligado!")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()