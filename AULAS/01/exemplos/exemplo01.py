from PySide6.QtWidgets import QApplication, QWidget

# Necessário apenas para o acesso a argumentos de comando de linha
import sys

# Só é preciso 1, e somente 1, instância de QApplication por aplicação.
# Passar o sys.argv serve para permitir que o aplicativo acesse argumentos de linha de comando.
# Se não for necessário, pode passar uma lista vazia: QApplication([])
app = QApplication(sys.argv)

# Criar uma janela, que é um widget
window = QWidget()
window.show() # Janelas não são visíveis por padrão, então precisamos mostrar a janela.

# Iniciar o loop de eventos da aplicação. O programa ficará aqui até que a janela seja fechada.
app.exec()