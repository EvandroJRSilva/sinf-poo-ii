import time

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.counter = 0

        layout = QVBoxLayout()

        self.label = QLabel("Início")
        button = QPushButton("PRE-RI-GO!")
        button.pressed.connect(self.oh_no)

        layout.addWidget(self.label)
        layout.addWidget(button)

        w = QWidget()
        w.setLayout(layout)
        self.setCentralWidget(w)

        # Outra possibilidade de fazer a Janela Principal ser mostrada
        self.show()

        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.recurring_timer)
        self.timer.start()

    def oh_no(self):
        time.sleep(5)

    def recurring_timer(self):
        self.counter += 1
        self.label.setText(f"Counter: {self.counter}")


app = QApplication([])
window = MainWindow()
# Aqui não tem window.show() por causa da linha 32
app.exec()