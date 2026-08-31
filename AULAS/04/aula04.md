# Aula 04

## *Dialogs* e *Alerts*

*Dialogs* são componentes de interface gráfica que permitem ao programa se comunicar com o usuário. São comumente usados para abrir/salvar arquivos, configurações, preferências, etc.

Costumam ser pequenas janelas modais (ou **bloqueantes**) que aparecem sobre a aplicação principal até serem fechadas. O Qt fornece um conjunto de *dialogs* nativos para os casos mais comuns.

No Qt, utilizamos os *dialog boxes* (ou *caixas de diálogo*) com a classe [`QDialog`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QDialog.html#PySide6.QtWidgets.QDialog). Vejamos um [exemplo](exemplos/exemplo01.py):

```python
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
```

Enquanto o QDialog permite a criação de um *dialog* complexo, em muitas das situações queremos apenas utilizar mensagens simples, que funcionem como **alertas**. Isso pode ser feito com a classe [`QMessageBox`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QMessageBox.html#PySide6.QtWidgets.QMessageBox).

Da mesma forma que o [`QDialog`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QDialog.html#PySide6.QtWidgets.QDialog), o [`QMessageBox`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QMessageBox.html#PySide6.QtWidgets.QMessageBox) também possui seus [botões](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QMessageBox.html#PySide6.QtWidgets.QMessageBox.StandardButton), e possuem também [ícones próprios](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QMessageBox.html#PySide6.QtWidgets.QMessageBox.Icon).

[Exemplo](exemplos/exemplo02.py):

```python
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Message Box")
        self.setMinimumWidth(300)
        self.setMinimumHeight(200)
        
        botao = QPushButton("Clique aqui para aparecer um Message Box")
        botao.clicked.connect(self.botao_clicado)
        self.setCentralWidget(botao)
        
    def botao_clicado(self, s):
        # FORMA 1
         message_box = QMessageBox(self) # passando a MainWindow como parent
         message_box.setWindowTitle("Eu tenho uma pergunta")
         message_box.setText("Você está estudando?")
         message_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
         botao = message_box.exec()
        
        # FORMA 2 - utilizando as funções estáticas
        # botao = QMessageBox.question(self, "Eu tenho uma pergunta", "Você está estudando?")
        #
        if botao == QMessageBox.StandardButton.Yes:
            print("SIM!")
        else:
            print("NÃO!")
            
app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
```

## Criando janelas adicionais

As janelas de *dialog* são bloqueantes, ou seja, enquanto você não fechá-las, elas vão deixar a janela principal travada. Entretanto, existem situações onde podem ser necessárias uma ou mais novas janelas da aplicação que não interrompam a janela principal.

Apesar de ser relativamente simples e direto o processo de abrir novas janelas, é preciso sempre ter em mente a forma como elas funcionam, são criadas, escondidas, etc.

De início, vamos lembrar que **qualquer widget sem um nó pai é uma janela**. Ou seja, para criar uma nova janela, basta instanciar qualquer widget. [Exemplo](exemplos/exemplo03.py):

```python
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel

class OutraJanela(QWidget):
    """
    Widget genérico, sem pai, portanto, é uma janela
    """
    
    def __init__(self, texto):
        super().__init__()
        
        layout = QVBoxLayout()
        self.label = QLabel(texto)
        layout.addWidget(self.label)
        self.setLayout(layout)
        
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Instanciando aqui
        # ----------------------------------------------------------------
        self.nova_janela1 = OutraJanela("Janela 1")
        self.nova_janela2 = OutraJanela("Janela 2")
        # ----------------------------------------------------------------
        
        layout = QVBoxLayout()
        
        botao1 = QPushButton("Clique aqui para abrir a janela 1")
        botao1.clicked.connect(self.mostrar_janela1)
        # botao1.clicked.connect(lambda checked: self.mostrar_janela(self.nova_janela1))
        layout.addWidget(botao1)
        
        botao2 = QPushButton("Clique aqui para abrir a janela 2")
        botao2.clicked.connect(self.mostrar_janela2)
        # botao2.clicked.connect(lambda checked: self.mostrar_janela(self.nova_janela2))
        layout.addWidget(botao2)
        
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
    
    def mostrar_janela1(self):
        if self.nova_janela1.isVisible():
            self.nova_janela1.hide()
        else:
            self.nova_janela1.show()
        
        
    def mostrar_janela2(self):
        if self.nova_janela2.isVisible():
            self.nova_janela2.hide()
        else:
            self.nova_janela2.show()
            
    def mostrar_janela(self, janela):
        if janela.isVisible():
            janela.hide()
        else:
            janela.show()
        
app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
```

## Exercícios

### `QDialog`

#### Fácil

1. Crie uma classe que herde de `QDialog` e mostre uma janela vazia com título “Meu Diálogo”.
2. Use `QDialog` com `QPushButton` “OK” que fecha o diálogo ao clicar.
3. Configure `exec()` para abrir um QDialog modal simples.
4. Crie QDialog com `QLineEdit` e botão “Confirmar”.
5. Adicione um `QLabel` “Digite seu nome” dentro de um `QDialog`.
6. Use `QDialogButtonBox` com botões OK e Cancel em um `QDialog`.
7. Crie `QDialog` que aparece ao clicar em um botão da janela principal.
8. Configure `setFixedSize(300, 200)` em um QDialog.
9. Use `show()` (não modal) em um `QDialog` com um `QCheckBox`.
10. Crie `QDialog` com `QComboBox` contendo 3 opções.
11. Adicione um `QSpinBox` dentro de um `QDialog` simples.
12. Configure `setWindowTitle("Configurações")` em um `QDialog`.
13. Use `accept()` e `reject()` manualmente em botões de `QDialog`.
14. Crie `QDialog` com ícone via `setWindowIcon`.
15. Mostre um `QDialog` com `QTextEdit` de uma linha.

#### Médio

1. Crie `QDialog` com layout `QVBoxLayout` contendo `label` + `lineedit` + `buttonBox`.
2. Implemente `QDialog` que retorna o texto digitado via `exec()` e `result()`.
3. Use `QDialog` com sinal `finished(int)` conectado a um slot na janela principal.
4. Crie `QDialog` com duas abas usando `QTabWidget` dentro dele.
5. Configure `QDialog` que salva dados em `QSettings` ao clicar em OK.
6. Implemente `QDialog` com validação: desabilita botão OK se campo estiver vazio.
7. Use `QFileDialog` como base e crie um diálogo customizado de seleção de cor.
8. Crie `QDialog` com `QTableWidget` e botões para adicionar/remover linhas.
9. Implemente diálogo modal que bloqueia apenas a janela pai (não toda aplicação).
10. Use `QInputDialog` como referência e crie `QDialog` personalizado equivalente.

#### Difícil

1. Desenvolva `QDialog` com `QStackedLayout` que muda entre “Dados” e “Preview” com botões Avançar/Voltar e validação em cada etapa.
2. Crie `QDialog` customizado com animação de entrada (`QPropertyAnimation`) e sinais para notificar a janela principal.
3. Implemente um diálogo de login com `QLineEdit` (senha mascarada), `QCheckBox` “lembrar”, e autenticação simulada via slot.
4. Desenvolva `QDialog` que carrega e edita um objeto complexo (dataclass) e emite sinal `dataChanged` ao aceitar.
5. Crie um sistema de diálogos encadeados (`wizard`) onde o fechamento de um abre o próximo com passagem de dados via sinais.

### `QMessageBox`

#### Fácil

1. Mostre `QMessageBox.information()` com título “Sucesso” e texto “Operação concluída”.
2. Use `QMessageBox.warning()` com botão OK.
3. Crie `QMessageBox.question()` perguntando “Deseja sair?” com Yes/No.
4. Configure `QMessageBox.critical()` com ícone de erro.
5. Use `exec()` em `QMessageBox` e verifique o botão clicado.
6. Adicione `QMessageBox` com texto formatado em HTML simples.
7. Crie alerta com `setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)`.
8. Mostre `QMessageBox` a partir de um slot de botão na janela principal.
9. Use `QMessageBox.about()` com informações da aplicação.
10. Configure `setIconPixmap` com um ícone personalizado em `QMessageBox`.
11. Crie `QMessageBox` com título vazio e apenas texto.
12. Use `QMessageBox` com botão “Sim”, “Não” e “Cancelar”.
13. Mostre alerta de confirmação ao tentar fechar a janela.
14. Crie `QMessageBox` com `setDetailedText("Log completo...")`.
15. Use `information()` com `timeout` simulado via `QTimer`.

#### Médio

1. Crie QMessageBox com três botões customizados e verifique qual foi clicado via `clickedButton()`.
2. Implemente função que retorna `QMessageBox` configurável (tipo, ícone, texto) via parâmetros.
3. Use `QMessageBox` com sinal `buttonClicked` conectado a um slot.
4. Crie alerta que aparece no centro da tela usando `move()`.
5. Implemente `QMessageBox` com checkbox “Não mostrar novamente” e salve em `QSettings`.
6. Crie sequência de alertas: sucesso → confirmação → erro em slots encadeados.
7. Use `QMessageBox` com `setStyleSheet` para mudar cores.
8. Implemente alerta de progresso falso (com `QProgressBar` dentro via `setWidget`).
9. Crie `QMessageBox` que usa `QTimer` para fechar automaticamente após 5 segundos.
10. Use `QMessageBox` para escolha de múltiplas opções com `QCheckBox` dentro.

#### Difícil

1. Desenvolva um sistema de alertas centralizado que usa fila (`QQueue`) e mostra um por vez com sinais.
2. Crie QMessageBox customizado que herda e adiciona `QLineEdit` para resposta rápida.
3. Implemente alertas assíncronos que são disparados de `QThread` e mostrados na thread principal via signal.
4. Desenvolva “Toast” style usando `QMessageBox` transparente + animação + timer de auto-fechamento.
5. Crie framework de notificação com diferentes níveis (info, success, warning, error) usando `QMessageBox` + ícones SVG e sons.

### Múltiplas janelas

#### Fácil

1. Crie uma segunda `QMainWindow` e mostre-a com `show()` ao clicar em um botão da principal.
2. Use `QMainWindow` secundária com título “Janela 2” e um `QLabel`.
3. Configure `setParent(janela_principal)` em uma janela secundária.
4. Crie duas janelas independentes que aparecem ao mesmo tempo.
5. Use `hide()` e `show()` para alternar entre janela principal e secundária.
6. Crie janela filha com `Qt.Window` flag e botão para fechar.
7. Adicione `QAction` “Abrir Janela Nova” no menu da principal que abre outra janela.
8. Configure janela secundária com tamanho fixo 400x300.
9. Crie três janelas e feche todas com um botão na principal.
10. Use `activateWindow()` para trazer janela secundária para frente.
11. Crie janela com `setWindowModality(Qt.ApplicationModal)`.
12. Adicione `QToolBar` na janela secundária com `QAction` “Fechar”.
13. Use `QMainWindow` como popup com menuBar simples.
14. Crie janela que recebe texto da principal via construtor.
15. Mostre janela secundária como `Qt.Tool` (sem barra de título completa).

#### Médio

1. Implemente comunicação entre janelas usando sinais customizados (`janelaSecundaria.sinalEnviado.connect()`).
2. Crie gerenciador de janelas que limita a 3 janelas abertas.
3. Use `QApplication` para listar todas janelas abertas (`allWindows()`).
4. Crie janela MDI simulada com múltiplas `QMainWindow` dentro de `QMainWindow`.
5. Implemente passagem de dados bidirecional entre duas janelas via slots.
6. Configure janelas que salvam posição e tamanho com `QSettings` ao fechar.
7. Crie janela secundária que emite sinal quando fechada (`destroyed`).
8. Use `QDialog` como janela flutuante e `QMainWindow` como principal.
9. Implemente sincronização de `QTableWidget` entre duas janelas abertas.
10. Crie botão “Tile” que organiza duas janelas lado a lado na tela.

#### Difícil

1. Desenvolva um sistema de múltiplas janelas com dockable (`QDockWidget`) e possibilidade de `detach`/`reattach`.
2. Crie gerenciador de documentos (multi-document interface) com sinais de “janela ativa mudou”.
3. Implemente comunicação via `QSharedMemory` entre duas instâncias de aplicação (janelas).
4. Desenvolva janela secundária com `QThread` que atualiza em tempo real e envia dados via signal para principal.
5. Crie sistema completo de workspace com múltiplas janelas, toolbar compartilhada, menu dinâmico e persistência de layout.

### Exercícios que envolvem todos os tópicos vistos até então

#### Fácil

1. Crie `QMainWindow` com `QVBoxLayout`, `QToolBar` (“Nova Janela”), menu “Arquivo > Abrir Diálogo”, ao clicar abre `QDialog` com `QMessageBox` de boas-vindas e sinal que atualiza `QLabel` da principal.
2. Use `QHBoxLayout`, `QAction` no menu “Ajuda > Sobre” que mostra `QMessageBox`, e botão que abre janela secundária simples.
3. Configure `QGridLayout`, `QToolBar` com “Alert”, menu “Editar”, clique em `QAction` mostra `QMessageBox.question` e, se Yes, abre `QDialog`.
4. Crie `QStackedLayout` na principal, `QAction` “Janela 2” no toolbar abre janela secundária que envia sinal para trocar página.
5. Adicione `QPushButton` em `QDialog`, ao aceitar mostra `QMessageBox` e emite sinal para `QTableWidget` na janela principal.
6. Use menu “Janela > Nova” que abre `QMainWindow` secundária com `QToolBar` e botão que dispara `QMessageBox`.
7. Crie `QDialog` com `QLineEdit`, botão OK mostra `QMessageBox` e fecha, enviando texto via sinal para `QLabel` da principal.
8. Configure `QVBoxLayout` + `QToolBar`, menu “Arquivo > Sair” mostra `QMessageBox.confirm` e, se sim, fecha todas janelas.
9. Adicione `QAction` “Diálogo” na toolbar que abre `QDialog` modal com alert dentro e evento `closeEvent` que atualiza statusBar.
10. Use `QHBoxLayout`, menu “Ver > Alerta”, clique mostra `QMessageBox` e abre janela secundária com `QLabel` atualizado via slot.

#### Médio

1. Desenvolva `QMainWindow` com `QGridLayout`, `QToolBar` e `menuBar` completos; `QAction` “Login” abre `QDialog` de login → se OK mostra `QMessageBox` sucesso e abre janela secundária com dados passados via sinal.
2. Crie dashboard com `QVBoxLayout` + `QSplitter`, toolbar com “Nova Janela”, menu “Ferramentas > Alertas”, sinais para sincronizar `QTableWidget` entre 3 janelas abertas e evento resize que reposiciona.
3. Use `QStackedLayout` na principal, `QAction` no menu “Diálogos” abre `QDialog` com `QTabWidget`, botão dentro dispara `QMessageBox` e sinal que muda página na principal.
4. Implemente aplicação com múltiplas janelas, `QToolBar` compartilhada via `QActionGroup`, menu dinâmico, `QDialog` de configuração que salva em `QSettings` e atualiza todas janelas via sinais.
5. Crie `QMainWindow` com `QHBoxLayout`, botão abre `QDialog` → ao aceitar mostra `QMessageBox` e abre janela flutuante que captura keyPressEvent para atualizar gráfico na principal.
6. Configure sistema com `QGridLayout`, toolbar “Ações”, menu “Arquivo”, onde cada `QAction` abre um tipo diferente (`QDialog` / `QMessageBox` / Janela) e todos se comunicam via sinais customizados.
7. Desenvolva editor com `QVBoxLayout` principal, `QToolBar`, `menuBar`, botão “Exportar” abre `QDialog` com preview, botão OK mostra `QMessageBox` e abre janela secundária de relatório.

#### Difícil

1. Crie aplicação completa de gerenciamento: `QMainWindow` com `QGridLayout` + `QStackedLayout`, `QToolBar` arrastável, `menuBar` carregado dinamicamente, `QAction` “Novo Projeto” abre `QDialog` wizard (3 etapas) → ao finalizar mostra `QMessageBox` sucesso, abre 2 janelas secundárias sincronizadas via sinais, com eventos drag-and-drop, undo stack e atualização em tempo real entre todas.
2. Desenvolva dashboard médico simulado: múltiplas janelas (principal + monitor + relatório), `QHBoxLayout` responsivo, `QToolBar` com plugins, menu “Paciente > Abrir”, abre QDialog com tabs + validação, botão Salvar dispara `QMessageBox` customizado + sinal que atualiza `QTableView` e `QGraphicsView` em todas janelas abertas, incluindo resizeEvent adaptativo e `QThread` para simulação de dados.
3. Implemente editor de documentos avançado: `QMainWindow` com `QVBoxLayout` central, `QToolBar` full, `menuBar` extensível, `QAction` “Publicar” abre `QDialog` complexo com `QStackedLayout` interno, validação, ao aceitar mostra `QMessageBox` com opção detalhada, abre janela preview flutuante, tudo interconectado por sinais customizados, slots assíncronos, eventos de mouse/gestos, `QUndoStack` compartilhada e persistência de estado de todas janelas.