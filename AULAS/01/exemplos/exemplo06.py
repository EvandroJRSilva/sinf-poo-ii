import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Meu Aplicativo Querido")
        self.setFixedWidth(400)

        # Perceba que agora o botão é um atributo de MainWindow
        self.button = QPushButton("Clique Aqui!")
        self.button.clicked.connect(self.botao_clicado)

        self.setCentralWidget(self.button)

    def botao_clicado(self):
        self.button.setText("Você já clicou!")
        self.button.setEnabled(False)  # Desabilita o botão após o clique
        
        self.setWindowTitle("Meu Aplicativo de 1 clique só!")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()