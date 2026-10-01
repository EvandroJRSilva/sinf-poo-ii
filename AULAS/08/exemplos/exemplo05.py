import sys
import time
import traceback
import threading

from PySide6.QtCore import (QObject, QTimer, Signal)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow,
    QPushButton, QVBoxLayout, QWidget)


class WorkerSignals(QObject):
    """Sinais de uma thread de trabalho em execução.

    finished
        int thread_id

    error
        tuple (exctype, value, traceback.format_exc())

    result
        dados do objeto retornados do processamento, qualquer tipo

    progress
        tuple (thread_id, progress_value)
    """

    finished = Signal(int)   # thread_id
    error = Signal(tuple)
    result = Signal(object)
    progress = Signal(tuple)  # (thread_id, progress_value)


class Worker:
    """Thread de tarefa/trabalho.

    Usa `threading.Thread` nativo do Python para executar a função callback
    em segundo plano, comunicando-se com a UI por meio de sinais do Qt.

    :param fn: A função callback a ser executada nessa thread de trabalho.
               Args e kwargs inseridos serão passados para o executor (runner).
    :type fn: function
    :param args: Argumentos a serem passados para a função callback
    :param kwargs: "palavra=chave" a serem passados para a função callback
    """

    def __init__(self, fn, *args, **kwargs):
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()
        self.thread_id = kwargs.get("thread_id", 0)
        # Adiciona o callback de progresso aos kwargs
        self.kwargs["progress_callback"] = self.signals.progress

        # Cria a thread nativa do Python (daemon=True encerra junto com o app)
        self._thread = threading.Thread(target=self._run, daemon=True)

    def _run(self):
        """Método interno executado pela thread nativa."""
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

    def start(self):
        """Inicia a thread nativa."""
        self._thread.start()


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

        max_threads = threading.active_count()
        print(f"Usando threading nativo do Python (threads ativas: {max_threads})")

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
        self.thread_id += 1
        worker = Worker(self.execute_this_fn, thread_id=self.thread_id)
        worker.signals.result.connect(self.print_output)
        worker.signals.finished.connect(self.thread_complete)
        worker.signals.progress.connect(self.progress_fn)
        # Inicia a thread nativa do Python
        worker.start()

    def recurring_timer(self):
        self.counter += 1
        self.label.setText(f"Contador: {self.counter}")


app = QApplication([])
window = MainWindow()
app.exec()