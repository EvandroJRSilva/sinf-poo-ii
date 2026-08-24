import sys
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QApplication, QCheckBox, QLabel, QMainWindow, QStatusBar, QToolBar

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Barra de Ferramentas")
        
        label = QLabel("Um texto qualquer")
        # O namespace `Qt` tem muitos atributos para customizar widgets. 
        # Veja: http://doc.qt.io/qt-6/qt.html
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setCentralWidget(label)

        toolbar = QToolBar("Barra de ferramentas principal")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)
        
        botao_action = QAction(QIcon("AULAS/03/imagens/icons/bug.png"), "Botão", self)
        botao_action.setCheckable(True)
        botao_action.setStatusTip("O meu botão")
        botao_action.triggered.connect(self.toolbar_button_clicked)
        toolbar.addAction(botao_action)
        
        toolbar.addSeparator()
        
        botao_action2 = QAction(QIcon("AULAS/03/imagens/icons/android.png"), "Botão 2", self)
        botao_action2.setStatusTip("Meu outro botão")
        botao_action2.triggered.connect(self.toolbar_button_clicked)
        botao_action2.setCheckable(True)
        toolbar.addAction(botao_action2)

        toolbar.addSeparator()
        
        toolbar.addWidget(QLabel("Olares"))
        toolbar.addSeparator()
        toolbar.addWidget(QCheckBox())
        
        # Barra de status - para mostrar o nome dos botões
        self.setStatusBar(QStatusBar(self))
        
    def toolbar_button_clicked(self, s):
        print(s)
        

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()