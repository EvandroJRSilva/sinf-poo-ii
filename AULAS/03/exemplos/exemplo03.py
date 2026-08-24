import sys
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction, QIcon, QKeySequence
from PySide6.QtWidgets import QApplication,QCheckBox, QLabel, QMainWindow, QStatusBar, QToolBar

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MENUDOS")

        label = QLabel("Um texto qualquer")

        # O namespace `Qt` tem muitos atributos para customizar widgets. 
        # Veja: http://doc.qt.io/qt-6/qt.html
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Configurando o widcet central da janela. O widget vai expandir para ocupar todo o espaço da janela por padrão.
        self.setCentralWidget(label)

        toolbar = QToolBar("Barra de Ferramentas Principal")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        button_action = QAction(QIcon("AULAS/03/imagens/icons/bug.png"), "Botão1", self)
        button_action.setStatusTip("Um botão")
        button_action.triggered.connect(self.toolbar_button_clicked)
        button_action.setCheckable(True)
        # É possível usar atalhos de teclado usando nomes de teclas (e.g. Ctrl+p), 
        # identificadores do namespace Qt (e.g. Qt.CTRL + Qt.Key_P) 
        # ou identificadores agnósticos de sistema (e.g. QKeySequence.Print)
        button_action.setShortcut(QKeySequence("Ctrl+p"))
        toolbar.addAction(button_action)

        toolbar.addSeparator()

        button_action2 = QAction(QIcon("AULAS/03/imagens/icons/android.png"), "Botão2", self)
        button_action2.setStatusTip("Outro botão")
        button_action2.triggered.connect(self.toolbar_button_clicked)
        button_action2.setCheckable(True)
        toolbar.addAction(button_action2)

        toolbar.addWidget(QLabel("Olares"))
        toolbar.addWidget(QCheckBox())

        self.setStatusBar(QStatusBar(self))

        menu = self.menuBar()

        menu_arquivo = menu.addMenu("Arquivo")
        menu_arquivo.addAction(button_action)

        menu_arquivo.addSeparator()

        submenu_arquivo = menu_arquivo.addMenu("Submenu")

        submenu_arquivo.addAction(button_action2)

    def toolbar_button_clicked(self, s):
        print(s)


app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()