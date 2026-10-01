import time
from PySide6.QtCore import QRunnable, QThreadPool, QTimer, Slot
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow,
    QPushButton, QVBoxLayout, QWidget)

class Worker(QRunnable):
    """Thread de tarefa/trabalho."""

    @Slot()
    def run(self):
        """A tarefa de longa execução."""
        print("Thread iniciada")
        time.sleep(5)
        print("Thread completa")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
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

        self.show()

        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.recurring_timer)
        self.timer.start()

        self.threadpool = QThreadPool()
        thread_count = self.threadpool.maxThreadCount()
        print(f"Multithreading com o máximo de {thread_count} threads")

    def oh_no(self):
        worker = Worker()
        self.threadpool.start(worker)

    def recurring_timer(self):
        self.counter += 1
        self.label.setText(f"Counter: {self.counter}")


app = QApplication([])
window = MainWindow()
app.exec()