import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton, QDialogButtonBox, QLabel, QVBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("DIALOG")
        self.setMinimumWidth(300)
        self.setMinimumHeight(200)
        
        botao = QPushButton("Clique aqui para abrir um dialog")
        botao.clicked.connect(self.botao_clicado)
        
        self.setCentralWidget(botao)
    
    def botao_clicado(self, s):
        print(s)
        
        dialog = MeuDialog(self)
        if dialog.exec():
            print("Sucesso")
        else:
            print("Cancelado")
    
class MeuDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent) # passando parent para centralizar no parent
        
        self.setWindowTitle("EU SOU O DIALOG")
        
        # Botões específicos para o dialog. A lista de tipos pode ser vista em:
        #   https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QDialogButtonBox.html#PySide6.QtWidgets.QDialogButtonBox.StandardButton
        #
        # Vários botões podem ser adicionados da seguinte forma: (bt1 | bt2 | bt3 ...). Utilizando os botões de Dialog, 
        # o Qt vai organizá-los de acordo com a ordem padrão do sistema em que estiver executando.
        botoes_dialog = (QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        
        self.botoes = QDialogButtonBox(botoes_dialog)
        self.botoes.accepted.connect(self.accept)
        self.botoes.rejected.connect(self.reject)
        
        layout = QVBoxLayout()
        mensagem = QLabel("Algo de certo não está errado! Certo?")
        layout.addWidget(mensagem)
        layout.addWidget(self.botoes)
        self.setLayout(layout)
        
app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()