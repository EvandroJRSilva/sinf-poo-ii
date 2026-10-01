import sys
import time
import traceback

from PySide6.QtCore import (QObject, QRunnable, QThreadPool,
    QTimer, Signal, Slot)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow,
    QPushButton, QVBoxLayout, QWidget)

class WorkerSignals(QObject):
    """Sinais de uma thread de trabalho em execução.

    finished
        int thread_id

    error
        tuple (exctype, value, traceback.format_exc())

    result
        dados dos objeto retornados do processamento, qualquer tipo

    progress
        tuple (thread_id, progress_value)
    """

    finished = Signal(int)  # thread_id
    error = Signal(tuple)
    result = Signal(object)
    progress = Signal(tuple)  # (thread_id, progress_value)

class Worker(QRunnable):
    """Thread de tarefa/trabalho.

    Herda de QRunnable para lidar com a configuração, os sinais e o encerramento da thread de trabalho.

    :param callback: A função callback a ser executada nessa thread de trabalho.
                     Args e kwargs inseridos serão passados para o executor (runner).
    :type callback: function
    :param args: Argumentos a serem passados para a função callback
    :param kwargs: "palavras-chave" a serem passados para a função callback
    """

    def __init__(self, fn, *args, **kwargs):
        super().__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()
        self.thread_id = kwargs.get("thread_id", 0)
        # Add the callback to our kwargs
        self.kwargs["progress_callback"] = self.signals.progress

    @Slot()
    def run(self):
        try:
            result = self.fn(*self.args, **self.kwargs)
        except Exception:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)
        finally:
            self.signals.finished.emit(self.thread_id)

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.counter = 0
        self.thread_id = 0

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

        self.threadpool = QThreadPool()
        thread_count = self.threadpool.maxThreadCount()
        print(f"Multithreading com o máximo de {thread_count} threads")

        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.recurring_timer)
        self.timer.start()

    def progress_fn(self, data):
        thread_id, n = data
        print(f"THREAD #{thread_id}: {n:.1f}% concluída")

    def execute_this_fn(self, progress_callback, thread_id):
        for n in range(0, 5):
            time.sleep(1)
            progress = n * 100 / 4
            progress_callback.emit((thread_id, progress))
        return "Concluída."

    def print_output(self, s):
        print(s)

    def thread_complete(self, thread_id):
        print(f"THREAD #{thread_id} FINALIZADA!")

    def oh_no(self):
        # Pass the function to execute
        self.thread_id += 1
        worker = Worker(
            self.execute_this_fn, thread_id=self.thread_id
        )  # Any other args, kwargs are passed to the run function
        worker.signals.result.connect(self.print_output)
        worker.signals.finished.connect(self.thread_complete)
        worker.signals.progress.connect(self.progress_fn)
        # Execute
        self.threadpool.start(worker)

    def recurring_timer(self):
        self.counter += 1
        self.label.setText(f"Contador: {self.counter}")

# Por causa do notebook, precisamos ver se já existe uma instância do QApplication, caso contrário, criamos uma nova.
if not QApplication.instance():
    app = QApplication([])
else:
    app = QApplication.instance()

window = MainWindow()
app.exec()