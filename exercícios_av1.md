# Exercícios para a AV1

Para cada questão, analise o código e indique quais afirmações são verdadeiras e quais são falsas.

- [Exercícios para a AV1](#exercícios-para-a-av1)
  - [1](#1)
  - [2](#2)
  - [3](#3)
  - [4](#4)
  - [5](#5)
  - [6](#6)
  - [Gabarito](#gabarito)

## 1

```python
import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QCheckBox

class Janela(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cadastro Simples")
        self.setMinimumWidth(300)

        self.label = QLabel("Digite seu nome:")
        self.input_nome = QLineEdit()
        self.checkbox = QCheckBox("Aceito os termos")
        self.botao = QPushButton("Enviar")
        self.resultado = QLabel("")

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.input_nome)
        layout.addWidget(self.checkbox)
        layout.addWidget(self.botao)
        layout.addWidget(self.resultado)

        self.setLayout(layout)

        self.botao.clicked.connect(self.enviar)
        self.checkbox.stateChanged.connect(self.alternar_botao)

        self.botao.setEnabled(False)

    def alternar_botao(self):
        self.botao.setEnabled(self.checkbox.isChecked())

    def enviar(self):
        nome = self.input_nome.text()
        if nome:
            self.resultado.setText(f"Bem-vindo, {nome}!")
        else:
            self.resultado.setText("Digite um nome válido.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = Janela()
    janela.show()
    sys.exit(app.exec())
```

(&emsp;) O título da janela é "Cadastro Simples".<br>
(&emsp;) O programa utiliza a biblioteca `PySide6` para criar a interface gráfica.<br>
(&emsp;) Existe um `QLabel` com o texto "Digite seu nome:".<br>
(&emsp;) O botão "Enviar" começa desabilitado quando a janela é aberta.<br>
(&emsp;) O checkbox tem o texto "Aceito os termos".<br>
(&emsp;) O título da janela é "Cadastro de Usuário".<br>
(&emsp;) O programa usa a biblioteca `Tkinter` para criar a interface.<br>
(&emsp;) Não existe nenhum `QLineEdit` no código.<br>
(&emsp;) O botão "Enviar" começa habilitado quando a aplicação inicia.<br>
(&emsp;) O checkbox está marcado por padrão ao abrir a janela.<br>
(&emsp;) Quando o checkbox é marcado, o botão "Enviar" é habilitado automaticamente.<br>
(&emsp;) A função alternar_botao é conectada ao sinal `stateChanged` do checkbox.<br>
(&emsp;) O botão "Enviar" só fica habilitado se o checkbox estiver marcado.<br>
(&emsp;) A classe principal herda de `QWidget`.<br>
(&emsp;) O método enviar é chamado quando o botão "Enviar" é clicado.<br>
(&emsp;) O botão "Enviar" fica habilitado mesmo se o checkbox não estiver marcado.<br>
(&emsp;) A função alternar_botao está conectada ao sinal clicked do botão.<br>
(&emsp;) A aplicação não utiliza nenhum layout para organizar os widgets.<br>
(&emsp;) O método enviar é executado automaticamente ao iniciar o programa.<br>
(&emsp;) O checkbox está conectado ao método enviar.<br>
(&emsp;) Se o usuário deixar o campo de nome vazio e clicar em "Enviar", a mensagem exibida será "Digite um nome válido.".<br>
(&emsp;) A aplicação usa um `QVBoxLayout` para organizar verticalmente todos os widgets.<br>
(&emsp;) O método `__init__` da classe Janela chama `super().__init__()` para inicializar corretamente a classe pai.<br>
(&emsp;) A variável self.resultado é um QLabel que é atualizado tanto no sucesso quanto na falha da validação do nome.<br>
(&emsp;) O programa termina corretamente com `sys.exit(app.exec())` após a execução da aplicação Qt.<br>
(&emsp;) Se o nome estiver vazio, o programa não exibe nenhuma mensagem de erro.<br>
(&emsp;) O layout utilizado é `QHBoxLayout` (horizontal) em vez de vertical.<br>
(&emsp;) A conexão do sinal clicked do botão está feita dentro do método alternar_botao.<br>
(&emsp;) O texto de boas-vindas é mostrado mesmo quando o campo de nome está vazio.<br>
(&emsp;) A aplicação não importa o módulo `sys`, sendo desnecessário para rodar o programa.<br>

## 2

```python
import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import QAction, Qt

class NovaTarefaDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Nova Tarefa")

        self.input = QLineEdit()

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Descrição da tarefa:"))
        layout.addWidget(self.input)

        botao = QPushButton("Adicionar")
        botao.clicked.connect(self.accept)

        layout.addWidget(botao)
        self.setLayout(layout)

    def get_texto(self):
        return self.input.text()

class Janela(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lista de Tarefas")

        toolbar = QToolBar()
        self.addToolBar(toolbar)

        acao_add = QAction("Nova Tarefa", self)
        acao_add.triggered.connect(self.nova_tarefa)
        toolbar.addAction(acao_add)

        menu = self.menuBar().addMenu("Tarefas")
        menu.addAction(acao_add)

        central = QWidget()
        layout = QVBoxLayout()

        self.lista = QListWidget()
        self.checkbox = QCheckBox("Mostrar concluídas")
        self.status = QLabel("0 tarefas")

        layout.addWidget(self.lista)
        layout.addWidget(self.checkbox)
        layout.addWidget(self.status)

        central.setLayout(layout)
        self.setCentralWidget(central)

        self.lista.itemChanged.connect(self.atualizar_status)

    def nova_tarefa(self):
        dialogo = NovaTarefaDialog()
        if dialogo.exec():
            texto = dialogo.get_texto()

            if texto:
                item = QListWidgetItem(texto)
                item.setCheckState(Qt.Unchecked)
                self.lista.addItem(item)
                self.atualizar_status()
            else:
                QMessageBox.warning(self, "Erro", "Tarefa vazia!")

    def atualizar_status(self):
        total = self.lista.count()
        concluidas = sum(
            1 for i in range(total)
            if self.lista.item(i).checkState() == Qt.Checked
        )
        self.status.setText(f"{concluidas}/{total} concluídas")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = Janela()
    janela.show()
    sys.exit(app.exec())
```

(&emsp;) O título da janela principal é "Lista de Tarefas".<br>
(&emsp;) Existe uma toolbar com a ação "Nova Tarefa".<br>
(&emsp;) O menu "Tarefas" contém a ação "Nova Tarefa".<br>
(&emsp;) Existe um QListWidget para exibir as tarefas.<br>
(&emsp;) A janela secundária tem o título "Nova Tarefa".<br>
(&emsp;) O título da janela principal é "Sistema de Cadastro".<br>
(&emsp;) Não existe nenhuma toolbar no programa.<br>
(&emsp;) O menu se chama "Arquivo" em vez de "Tarefas".<br>
(&emsp;) Não existe nenhum `QListWidget` no código.<br>
(&emsp;) A janela de nova tarefa tem o título "Adicionar Tarefa".<br>
(&emsp;) Ao clicar em "Nova Tarefa" (na toolbar ou no menu), o método nova_tarefa é executado.<br>
(&emsp;) O diálogo `NovaTarefaDialog` possui um método `get_texto()` que retorna o conteúdo do `QLineEdit`.<br>
(&emsp;) As tarefas são adicionadas como `QListWidgetItem` com estado de checkbox não marcado (`Qt.Unchecked`).<br>
(&emsp;) Existe um checkbox chamado "Mostrar concluídas" na interface.<br>
(&emsp;) O label de status mostra a quantidade de tarefas concluídas em relação ao total.<br>
(&emsp;) O diálogo de nova tarefa é aberto usando `dialogo.show()` em vez de `dialogo.exec()`.<br>
(&emsp;) As novas tarefas são adicionadas já marcadas como concluídas.<br>
(&emsp;) O método `nova_tarefa` está conectado ao sinal clicked de um botão.<br>
(&emsp;) O checkbox "Mostrar concluídas" controla a visibilidade das tarefas concluídas.<br>
(&emsp;) O status é atualizado automaticamente apenas quando uma tarefa é adicionada.<br>
(&emsp;) O método atualizar_status percorre todos os itens da lista usando um loop for e conta quantos estão com `checkState() == Qt.Checked`.<br>
(&emsp;) A conexão `self.lista.itemChanged.connect(self.atualizar_status)` atualiza o status sempre que o estado de qualquer item da lista é alterado.<br>
(&emsp;) Se o usuário confirmar o diálogo e o texto da tarefa não estiver vazio, um novo `QListWidgetItem` é criado e adicionado à lista.<br>
(&emsp;) A classe Janela herda de `QMainWindow` e utiliza um widget central com `QVBoxLayout` para organizar a lista, o checkbox e o status.<br>
(&emsp;) Se o texto da nova tarefa estiver vazio, é exibido um `QMessageBox.warning` com a mensagem "Tarefa vazia!".<br>
(&emsp;) O método atualizar_status conta apenas as tarefas não concluídas.<br>
(&emsp;) As tarefas são armazenadas em uma lista Python comum (`list`) em vez de usar `QListWidget`.<br>
(&emsp;) O checkbox "Mostrar concluídas" filtra a lista para esconder ou mostrar tarefas concluídas.<br>
(&emsp;) O diálogo `NovaTarefaDialog` herda de `QMainWindow`.<br>
(&emsp;) O status é atualizado apenas no método `nova_tarefa`, sem usar o sinal `itemChanged`.<br>

## 3

```python
"""
Exemplo 1 — Sinais, Slots, Eventos e Widgets
Foco: QCheckBox, QLabel, QLineEdit, QPushButton,
      conexão de sinais/slots e override de eventos.
"""

import sys
from PySide6.QtCore import Qt, Signal, QObject
from PySide6.QtGui import QKeyEvent, QCloseEvent
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QCheckBox, QVBoxLayout, QMessageBox
)


# ── Objeto auxiliar que emite um sinal customizado ──────────────────────────
class Validador(QObject):
    """Emite 'validado' com True/False conforme a senha digitada."""
    validado = Signal(bool)

    SENHA_CORRETA = "pyside6"

    def verificar(self, texto: str) -> None:
        self.validado.emit(texto == self.SENHA_CORRETA)


# ── Widget principal ────────────────────────────────────────────────────────
class JanelaLogin(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Exemplo 1 — Login Simples")
        self.setMinimumWidth(340)

        self.validador = Validador()

        # ── Widgets ────────────────────────────────────────────────────────
        self.lbl_titulo = QLabel("<b>Bem-vindo!</b> Faça seu login.")
        self.lbl_titulo.setAlignment(Qt.AlignCenter)

        self.lbl_usuario = QLabel("Usuário:")
        self.edt_usuario = QLineEdit()
        self.edt_usuario.setPlaceholderText("Digite seu usuário…")

        self.lbl_senha = QLabel("Senha:")
        self.edt_senha = QLineEdit()
        self.edt_senha.setPlaceholderText("Digite sua senha…")
        self.edt_senha.setEchoMode(QLineEdit.Password)

        self.chk_mostrar = QCheckBox("Mostrar senha")

        self.btn_entrar = QPushButton("Entrar")
        self.btn_limpar = QPushButton("Limpar")

        self.lbl_status = QLabel("")
        self.lbl_status.setAlignment(Qt.AlignCenter)

        # ── Layout ─────────────────────────────────────────────────────────
        layout = QVBoxLayout(self)
        layout.setSpacing(8)
        layout.setContentsMargins(20, 20, 20, 20)

        for w in (
            self.lbl_titulo,
            self.lbl_usuario, self.edt_usuario,
            self.lbl_senha, self.edt_senha,
            self.chk_mostrar,
            self.btn_entrar, self.btn_limpar,
            self.lbl_status,
        ):
            layout.addWidget(w)

        # ── Conexões de sinais/slots ────────────────────────────────────────
        # Botões → ações diretas
        self.btn_entrar.clicked.connect(self._tentar_login)
        self.btn_limpar.clicked.connect(self._limpar_campos)

        # CheckBox alterna visibilidade da senha
        self.chk_mostrar.stateChanged.connect(self._alternar_echo)

        # Sinal customizado do Validador → slot que atualiza o status
        self.validador.validado.connect(self._atualizar_status)

        # Pressionar Enter no campo de senha dispara o login
        self.edt_senha.returnPressed.connect(self.btn_entrar.click)

        # Texto digitado no usuário → limpa mensagem de status
        self.edt_usuario.textChanged.connect(lambda _: self.lbl_status.clear())

    # ── Slots ──────────────────────────────────────────────────────────────
    def _tentar_login(self) -> None:
        usuario = self.edt_usuario.text().strip()
        senha   = self.edt_senha.text()

        if not usuario:
            self.lbl_status.setText("⚠️  Informe o usuário.")
            self.lbl_status.setStyleSheet("color: orange;")
            return

        # Delega a verificação ao Validador (emitirá o sinal 'validado')
        self.validador.verificar(senha)

    def _limpar_campos(self) -> None:
        self.edt_usuario.clear()
        self.edt_senha.clear()
        self.lbl_status.clear()
        self.chk_mostrar.setChecked(False)
        self.edt_usuario.setFocus()

    def _alternar_echo(self, estado: int) -> None:
        modo = QLineEdit.Normal if estado == Qt.Checked else QLineEdit.Password
        self.edt_senha.setEchoMode(modo)

    def _atualizar_status(self, sucesso: bool) -> None:
        if sucesso:
            self.lbl_status.setText("✅  Login realizado com sucesso!")
            self.lbl_status.setStyleSheet("color: green; font-weight: bold;")
        else:
            self.lbl_status.setText("❌  Senha incorreta. (dica: pyside6)")
            self.lbl_status.setStyleSheet("color: red;")

    # ── Eventos ───────────────────────────────────────────────────────────
    def keyPressEvent(self, event: QKeyEvent) -> None:
        """Limpa o status ao pressionar Escape."""
        if event.key() == Qt.Key_Escape:
            self._limpar_campos()
        else:
            super().keyPressEvent(event)

    def closeEvent(self, event: QCloseEvent) -> None:
        """Confirma antes de fechar."""
        resposta = QMessageBox.question(
            self, "Sair", "Deseja fechar o aplicativo?",
            QMessageBox.Yes | QMessageBox.No,
        )
        if resposta == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


# ── Entry-point ────────────────────────────────────────────────────────────
if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = JanelaLogin()
    janela.show()
    sys.exit(app.exec())
```

(&emsp;) O código usa a biblioteca `PySide6` para criar a interface gráfica.<br>
(&emsp;) A classe principal da janela herda de `QWidget`.<br>
(&emsp;) O campo de senha usa o modo `QLineEdit.Password` por padrão.<br>
(&emsp;) O título da janela é "Exemplo 1 — Login Simples".<br>
(&emsp;) A senha correta definida no Validador é "pyside6".<br>
(&emsp;) O código importa `QHBoxLayout`.<br>
(&emsp;) Existe um `QComboBox` na interface.<br>
(&emsp;) O mínimo de largura da janela é 300 pixels.<br>
(&emsp;) O placeholder do campo usuário é "Digite sua senha…".<br>
(&emsp;) O botão "Entrar" tem texto em minúsculas.<br>
(&emsp;) O checkbox "Mostrar senha" conecta ao método `_alternar_echo`.<br>
(&emsp;) Pressionar Enter no campo senha simula clique no botão Entrar.<br>
(&emsp;) Digitar no campo usuário limpa a mensagem de status.<br>
(&emsp;) O layout usa margens de 20 pixels em todos os lados.<br>
(&emsp;) O sinal validado do Validador conecta ao método `_atualizar_status`.<br>
(&emsp;) O botão Limpar conecta ao método `_tentar_login`.<br>
(&emsp;) Todos os widgets são adicionados ao layout usando `addWidget()`.<br>
(&emsp;) O `lbl_titulo` tem alinhamento `Qt.AlignLeft`.<br>
(&emsp;) O `spacing` do layout é 12 pixels.<br>
(&emsp;) O foco é definido no campo senha após limpar os campos.<br>
(&emsp;) Pressionar `Escape` globalmente chama `_limpar_campos()`.<br>
(&emsp;) O `closeEvent` confirma fechamento com `QMessageBox`.<br>
(&emsp;) O método `_tentar_login` verifica se usuário está vazio antes da senha.<br>
(&emsp;) No modo senha visível, usa `QLineEdit.Normal`.<br>
(&emsp;) O Validador emite sinal validado com `True` apenas se `senha == SENHA_CORRETA`.<br>
(&emsp;) O `keyPressEvent` é chamado apenas para o campo de senha.<br>
(&emsp;) O `closeEvent` aceita fechamento se resposta for `QMessageBox.No`.<br>
(&emsp;) O `_limpar_campos()` define foco no campo senha.<br>
(&emsp;) O `_atualizar_status()` é chamado diretamente no `_tentar_login()`.<br>
(&emsp;) O sinal validado passa dois parâmetros (`bool` e `string`).<br>

## 4

```python
import sys
from dataclasses import dataclass, field
from typing import Optional
from PySide6.QtCore import Qt, Signal, QObject
from PySide6.QtGui import QAction, QFont, QKeyEvent, QCloseEvent
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog,
    QLabel, QLineEdit, QPushButton, QCheckBox, QTextEdit, QComboBox,
    QVBoxLayout, QHBoxLayout, QGridLayout, QFormLayout, QScrollArea, 
    QDialogButtonBox, QMessageBox)


# ══════════════════════════════════════════════════════════════════════════════
# Modelo de dados
# ══════════════════════════════════════════════════════════════════════════════
@dataclass
class Contato:
    nome:      str
    email:     str
    telefone:  str
    grupo:     str = "Geral"
    favorito:  bool = False
    notas:     str = ""
    id:        int = field(default_factory=lambda: Contato._next_id())

    _counter: int = 0

    @staticmethod
    def _next_id() -> int:
        Contato._counter += 1
        return Contato._counter


# ══════════════════════════════════════════════════════════════════════════════
# Repositório (modelo) com sinais
# ══════════════════════════════════════════════════════════════════════════════
class RepositorioContatos(QObject):
    alterado = Signal()   # emitido a cada mudança

    def __init__(self) -> None:
        super().__init__()
        self._dados: list[Contato] = []
        self._popular_demo()

    def _popular_demo(self) -> None:
        demos = [
            Contato("Alice Souza",   "alice@email.com",   "(11) 91111-1111", "Trabalho",  True),
            Contato("Bruno Lima",    "bruno@email.com",   "(21) 92222-2222", "Amigos",    False),
            Contato("Carla Mendes",  "carla@email.com",   "(31) 93333-3333", "Família",   True),
            Contato("Diego Rocha",   "diego@email.com",   "(41) 94444-4444", "Geral",     False),
            Contato("Eva Ferreira",  "eva@email.com",     "(51) 95555-5555", "Trabalho",  False),
        ]
        for c in demos:
            self._dados.append(c)

    # CRUD ──────────────────────────────────────────────────────────────────
    def todos(self) -> list[Contato]:
        return list(self._dados)

    def buscar(self, termo: str) -> list[Contato]:
        t = termo.lower()
        return [c for c in self._dados
                if t in c.nome.lower() or t in c.email.lower()
                or t in c.telefone or t in c.grupo.lower()]

    def por_grupo(self, grupo: str) -> list[Contato]:
        if grupo == "Todos":
            return self.todos()
        return [c for c in self._dados if c.grupo == grupo]

    def adicionar(self, contato: Contato) -> None:
        self._dados.append(contato)
        self.alterado.emit()

    def atualizar(self, contato: Contato) -> None:
        for i, c in enumerate(self._dados):
            if c.id == contato.id:
                self._dados[i] = contato
                break
        self.alterado.emit()

    def remover(self, ids: list[int]) -> None:
        self._dados = [c for c in self._dados if c.id not in ids]
        self.alterado.emit()

    def grupos(self) -> list[str]:
        return ["Todos"] + sorted({c.grupo for c in self._dados})


# ══════════════════════════════════════════════════════════════════════════════
# Widget de linha de contato
# ══════════════════════════════════════════════════════════════════════════════
class LinhaContato(QWidget):
    selecionado   = Signal(int)    # id
    abrir_detalhe = Signal(int)    # id

    def __init__(self, contato: Contato, parent=None) -> None:
        super().__init__(parent)
        self.contato_id = contato.id
        self._montar(contato)

    def _montar(self, c: Contato) -> None:
        self.chk = QCheckBox()
        self.chk.stateChanged.connect(lambda _: self.selecionado.emit(self.contato_id))

        fav = QLabel("⭐" if c.favorito else "  ")
        fav.setFixedWidth(20)

        lbl_nome  = QLabel(f"<b>{c.nome}</b>")
        lbl_email = QLabel(c.email)
        lbl_email.setStyleSheet("color: #666; font-size: 12px;")
        lbl_tel   = QLabel(c.telefone)
        lbl_tel.setStyleSheet("color: #666; font-size: 12px;")

        lbl_grupo = QLabel(c.grupo)
        lbl_grupo.setStyleSheet(
            "background:#dde; color:#336; padding:1px 6px;"
            "border-radius:8px; font-size:11px;"
        )
        lbl_grupo.setFixedWidth(72)
        lbl_grupo.setAlignment(Qt.AlignCenter)

        btn_ver = QPushButton("Ver")
        btn_ver.setFixedSize(40, 26)
        btn_ver.clicked.connect(lambda: self.abrir_detalhe.emit(self.contato_id))

        info = QVBoxLayout()
        info.setSpacing(0)
        info.addWidget(lbl_nome)
        info.addWidget(lbl_email)

        hbox = QHBoxLayout(self)
        hbox.setContentsMargins(4, 4, 4, 4)
        hbox.addWidget(self.chk)
        hbox.addWidget(fav)
        hbox.addLayout(info, stretch=1)
        hbox.addWidget(lbl_tel)
        hbox.addWidget(lbl_grupo)
        hbox.addWidget(btn_ver)

    def marcado(self) -> bool:
        return self.chk.isChecked()


# ══════════════════════════════════════════════════════════════════════════════
# Diálogo: formulário de contato (novo / editar)
# ══════════════════════════════════════════════════════════════════════════════
class DialogoContato(QDialog):
    salvo = Signal(object)   # Contato

    GRUPOS = ["Geral", "Trabalho", "Amigos", "Família"]

    def __init__(self, contato: Optional[Contato] = None, parent=None) -> None:
        super().__init__(parent)
        self._contato_orig = contato
        self.setWindowTitle("Editar Contato" if contato else "Novo Contato")
        self.setMinimumWidth(360)
        self._construir()
        if contato:
            self._preencher(contato)

    def _construir(self) -> None:
        self.edt_nome  = QLineEdit(); self.edt_nome.setPlaceholderText("Nome completo")
        self.edt_email = QLineEdit(); self.edt_email.setPlaceholderText("email@exemplo.com")
        self.edt_tel   = QLineEdit(); self.edt_tel.setPlaceholderText("(00) 00000-0000")
        self.cmb_grupo = QComboBox(); self.cmb_grupo.addItems(self.GRUPOS)
        self.chk_fav   = QCheckBox("Marcar como favorito")
        self.edt_notas = QTextEdit(); self.edt_notas.setFixedHeight(70)
        self.edt_notas.setPlaceholderText("Observações…")

        form = QFormLayout()
        form.addRow("Nome *:",    self.edt_nome)
        form.addRow("E-mail *:",  self.edt_email)
        form.addRow("Telefone:",  self.edt_tel)
        form.addRow("Grupo:",     self.cmb_grupo)
        form.addRow("",           self.chk_fav)
        form.addRow("Notas:",     self.edt_notas)

        botoes = QDialogButtonBox(QDialogButtonBox.Save | QDialogButtonBox.Cancel)
        botoes.accepted.connect(self._salvar)
        botoes.rejected.connect(self.reject)

        layout = QVBoxLayout(self)
        layout.addLayout(form)
        layout.addWidget(botoes)

    def _preencher(self, c: Contato) -> None:
        self.edt_nome.setText(c.nome)
        self.edt_email.setText(c.email)
        self.edt_tel.setText(c.telefone)
        idx = self.cmb_grupo.findText(c.grupo)
        if idx >= 0:
            self.cmb_grupo.setCurrentIndex(idx)
        self.chk_fav.setChecked(c.favorito)
        self.edt_notas.setPlainText(c.notas)

    def _salvar(self) -> None:
        nome  = self.edt_nome.text().strip()
        email = self.edt_email.text().strip()
        if not nome or not email:
            QMessageBox.warning(self, "Campos obrigatórios",
                                "Preencha pelo menos Nome e E-mail.")
            return

        if self._contato_orig:
            c = Contato(
                nome=nome, email=email,
                telefone=self.edt_tel.text().strip(),
                grupo=self.cmb_grupo.currentText(),
                favorito=self.chk_fav.isChecked(),
                notas=self.edt_notas.toPlainText(),
                id=self._contato_orig.id,
            )
        else:
            c = Contato(
                nome=nome, email=email,
                telefone=self.edt_tel.text().strip(),
                grupo=self.cmb_grupo.currentText(),
                favorito=self.chk_fav.isChecked(),
                notas=self.edt_notas.toPlainText(),
            )
        self.salvo.emit(c)
        self.accept()


# ══════════════════════════════════════════════════════════════════════════════
# Janela adicional: detalhes do contato
# ══════════════════════════════════════════════════════════════════════════════
class JanelaDetalhe(QMainWindow):
    editar_solicitado = Signal(int)

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setWindowTitle("Detalhes do Contato")
        self.setMinimumSize(320, 280)
        self._contato_id: Optional[int] = None
        self._construir()

    def _construir(self) -> None:
        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(8)

        self.lbl_nome  = QLabel()
        f = QFont(); f.setPointSize(16); f.setBold(True)
        self.lbl_nome.setFont(f)

        grid = QGridLayout()
        rotulos = ["E-mail:", "Telefone:", "Grupo:", "Favorito:", "Notas:"]
        self.valores: dict[str, QLabel] = {}
        for i, r in enumerate(rotulos):
            grid.addWidget(QLabel(r), i, 0, Qt.AlignRight | Qt.AlignTop)
            val = QLabel()
            val.setWordWrap(True)
            grid.addWidget(val, i, 1)
            self.valores[r] = val

        btn_editar = QPushButton("✏️  Editar")
        btn_editar.clicked.connect(lambda: self.editar_solicitado.emit(self._contato_id))

        layout.addWidget(self.lbl_nome)
        layout.addLayout(grid)
        layout.addStretch()
        layout.addWidget(btn_editar, alignment=Qt.AlignRight)

    def exibir(self, c: Contato) -> None:
        self._contato_id = c.id
        self.setWindowTitle(f"Contato — {c.nome}")
        self.lbl_nome.setText(("⭐ " if c.favorito else "") + c.nome)
        self.valores["E-mail:"].setText(c.email)
        self.valores["Telefone:"].setText(c.telefone or "—")
        self.valores["Grupo:"].setText(c.grupo)
        self.valores["Favorito:"].setText("Sim" if c.favorito else "Não")
        self.valores["Notas:"].setText(c.notas or "—")
        self.show()
        self.raise_()


# ══════════════════════════════════════════════════════════════════════════════
# Janela principal
# ══════════════════════════════════════════════════════════════════════════════
class AppContatos(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Exemplo 5 — Gerenciador de Contatos")
        self.setMinimumSize(680, 520)

        self.repo          = RepositorioContatos()
        self.janela_detalhe = JanelaDetalhe(self)
        self._selecionados: set[int] = set()

        self._criar_menu()
        self._criar_toolbar()
        self._criar_ui()
        self._criar_statusbar()

        self.repo.alterado.connect(self._recarregar)
        self.janela_detalhe.editar_solicitado.connect(self._editar_por_id)
        self._recarregar()

    # ── Menu ───────────────────────────────────────────────────────────────
    def _criar_menu(self) -> None:
        mb = self.menuBar()

        # Contatos
        m = mb.addMenu("&Contatos")
        for label, shortcut, slot in [
            ("&Novo…",             "Ctrl+N", self._novo_contato),
            ("&Remover selecionados", "Del", self._remover_selecionados),
        ]:
            a = QAction(label, self, shortcut=shortcut)
            a.triggered.connect(slot)
            m.addAction(a)
        m.addSeparator()
        a_sair = QAction("Sai&r", self, shortcut="Ctrl+Q")
        a_sair.triggered.connect(self.close)
        m.addAction(a_sair)

        # Ver
        m_ver = mb.addMenu("&Ver")
        for label, grupo in [
            ("Todos",    "Todos"),
            ("Trabalho", "Trabalho"),
            ("Amigos",   "Amigos"),
            ("Família",  "Família"),
            ("Geral",    "Geral"),
        ]:
            a = QAction(label, self)
            a.triggered.connect(lambda _, g=grupo: self._filtrar_grupo(g))
            m_ver.addAction(a)

        # Ajuda
        m_ajuda = mb.addMenu("A&juda")
        a_sobre = QAction("Sobre…", self)
        a_sobre.triggered.connect(lambda: QMessageBox.information(
            self, "Sobre",
            "Gerenciador de Contatos\nExemplo 5 — PySide6\n\n"
            "Demonstra todos os recursos cobertos nos exemplos 1–4."
        ))
        m_ajuda.addAction(a_sobre)

    # ── Toolbar ────────────────────────────────────────────────────────────
    def _criar_toolbar(self) -> None:
        tb = self.addToolBar("Ações")
        tb.setMovable(False)
        acoes = [
            ("➕ Novo",     self._novo_contato),
            ("✏️ Editar",   self._editar_selecionado),
            ("🗑 Remover",  self._remover_selecionados),
            ("☑️ Sel. todos", self._selecionar_todos),
        ]
        for texto, slot in acoes:
            tb.addAction(texto).triggered.connect(slot)

    # ── Statusbar ──────────────────────────────────────────────────────────
    def _criar_statusbar(self) -> None:
        self.lbl_total = QLabel("0 contatos")
        self.lbl_sel   = QLabel("0 selecionados")
        sb = self.statusBar()
        sb.addPermanentWidget(self.lbl_sel)
        sb.addPermanentWidget(self.lbl_total)

    # ── UI central ─────────────────────────────────────────────────────────
    def _criar_ui(self) -> None:
        central = QWidget()
        self.setCentralWidget(central)
        vbox = QVBoxLayout(central)
        vbox.setContentsMargins(10, 10, 10, 10)
        vbox.setSpacing(8)

        # Barra de filtro
        hfiltro = QHBoxLayout()
        lbl_busca = QLabel("🔍")
        self.edt_busca = QLineEdit()
        self.edt_busca.setPlaceholderText("Buscar por nome, e-mail, telefone ou grupo…")
        self.edt_busca.textChanged.connect(self._filtrar_texto)
        self.edt_busca.setClearButtonEnabled(True)

        self.cmb_grupo = QComboBox()
        self.cmb_grupo.addItems(self.repo.grupos())
        self.cmb_grupo.currentTextChanged.connect(self._filtrar_grupo)

        hfiltro.addWidget(lbl_busca)
        hfiltro.addWidget(self.edt_busca, stretch=1)
        hfiltro.addWidget(QLabel("Grupo:"))
        hfiltro.addWidget(self.cmb_grupo)
        vbox.addLayout(hfiltro)

        # Área de scroll com contatos
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.container = QWidget()
        self.lista_layout = QVBoxLayout(self.container)
        self.lista_layout.setAlignment(Qt.AlignTop)
        self.lista_layout.setSpacing(2)
        self.scroll.setWidget(self.container)
        vbox.addWidget(self.scroll, stretch=1)

        # Rodapé
        hfooter = QHBoxLayout()
        btn_novo    = QPushButton("➕ Novo Contato")
        btn_remover = QPushButton("🗑 Remover Selecionados")
        btn_novo.clicked.connect(self._novo_contato)
        btn_remover.clicked.connect(self._remover_selecionados)
        hfooter.addStretch()
        hfooter.addWidget(btn_novo)
        hfooter.addWidget(btn_remover)
        vbox.addLayout(hfooter)

    # ── Renderização da lista ──────────────────────────────────────────────
    def _recarregar(self) -> None:
        termo = self.edt_busca.text().strip() if hasattr(self, "edt_busca") else ""
        grupo = self.cmb_grupo.currentText() if hasattr(self, "cmb_grupo") else "Todos"
        contatos = self.repo.buscar(termo) if termo else self.repo.por_grupo(grupo)
        self._renderizar(contatos)

        # Atualiza combo de grupos preservando seleção
        grupos = self.repo.grupos()
        self.cmb_grupo.blockSignals(True)
        atual = self.cmb_grupo.currentText()
        self.cmb_grupo.clear()
        self.cmb_grupo.addItems(grupos)
        idx = self.cmb_grupo.findText(atual)
        self.cmb_grupo.setCurrentIndex(max(0, idx))
        self.cmb_grupo.blockSignals(False)

    def _renderizar(self, contatos: list[Contato]) -> None:
        # Remove widgets antigos
        while self.lista_layout.count():
            item = self.lista_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
        self._selecionados.clear()

        for c in contatos:
            linha = LinhaContato(c)
            linha.selecionado.connect(self._toggle_selecao)
            linha.abrir_detalhe.connect(self._abrir_detalhe)
            self.lista_layout.addWidget(linha)

        self.lbl_total.setText(f"{len(contatos)} contato(s)")
        self.lbl_sel.setText("0 selecionados")

        if not contatos:
            aviso = QLabel("Nenhum contato encontrado.")
            aviso.setAlignment(Qt.AlignCenter)
            aviso.setStyleSheet("color: #999; font-style: italic; padding: 20px;")
            self.lista_layout.addWidget(aviso)

    def _toggle_selecao(self, cid: int) -> None:
        if cid in self._selecionados:
            self._selecionados.discard(cid)
        else:
            self._selecionados.add(cid)
        self.lbl_sel.setText(f"{len(self._selecionados)} selecionado(s)")

    def _selecionar_todos(self) -> None:
        for i in range(self.lista_layout.count()):
            item = self.lista_layout.itemAt(i)
            if item and isinstance(item.widget(), LinhaContato):
                linha: LinhaContato = item.widget()
                linha.chk.setChecked(True)

    def _filtrar_texto(self, texto: str) -> None:
        contatos = self.repo.buscar(texto) if texto else self.repo.por_grupo(
            self.cmb_grupo.currentText()
        )
        self._renderizar(contatos)

    def _filtrar_grupo(self, grupo: str) -> None:
        self.edt_busca.clear()
        self._renderizar(self.repo.por_grupo(grupo))

    # ── CRUD ──────────────────────────────────────────────────────────────
    def _novo_contato(self) -> None:
        dlg = DialogoContato(parent=self)
        dlg.salvo.connect(self.repo.adicionar)
        dlg.exec()

    def _editar_por_id(self, cid: int) -> None:
        contato = next((c for c in self.repo.todos() if c.id == cid), None)
        if contato:
            self._abrir_edicao(contato)

    def _editar_selecionado(self) -> None:
        if len(self._selecionados) != 1:
            QMessageBox.information(self, "Selecione um contato",
                                    "Selecione exatamente um contato para editar.")
            return
        cid = next(iter(self._selecionados))
        self._editar_por_id(cid)

    def _abrir_edicao(self, contato: Contato) -> None:
        dlg = DialogoContato(contato=contato, parent=self)
        dlg.salvo.connect(self.repo.atualizar)
        dlg.exec()

    def _abrir_detalhe(self, cid: int) -> None:
        contato = next((c for c in self.repo.todos() if c.id == cid), None)
        if contato:
            self.janela_detalhe.exibir(contato)

    def _remover_selecionados(self) -> None:
        ids = list(self._selecionados)
        if not ids:
            QMessageBox.warning(self, "Nada selecionado",
                                "Marque ao menos um contato para remover.")
            return
        resp = QMessageBox.question(
            self, "Confirmar remoção",
            f"Remover {len(ids)} contato(s) permanentemente?",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No
        )
        if resp == QMessageBox.Yes:
            self.repo.remover(ids)
            self.statusBar().showMessage(f"{len(ids)} contato(s) removido(s).", 3000)

    # ── Eventos ───────────────────────────────────────────────────────────
    def keyPressEvent(self, event: QKeyEvent) -> None:
        if event.key() == Qt.Key_N and event.modifiers() == Qt.ControlModifier:
            self._novo_contato()
        elif event.key() == Qt.Key_Delete:
            self._remover_selecionados()
        elif event.key() == Qt.Key_Escape:
            self.edt_busca.clear()
        else:
            super().keyPressEvent(event)

    def closeEvent(self, event: QCloseEvent) -> None:
        resp = QMessageBox.question(
            self, "Sair",
            "Deseja fechar o Gerenciador de Contatos?",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No
        )
        if resp == QMessageBox.Yes:
            self.janela_detalhe.close()
            event.accept()
        else:
            event.ignore()


# ── Entry-point ────────────────────────────────────────────────────────────
if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = AppContatos()
    janela.show()
    sys.exit(app.exec())

```

(&emsp;) O código usa `dataclass` `Contato` com campos `nome`, `email`, `telefone`, `grupo`.<br>
(&emsp;) `RepositorioContatos` popula 5 contatos demo na inicialização.<br>
(&emsp;) `LinhaContato` mostra ícone ⭐ para contatos favoritos.<br>
(&emsp;) `DialogoContato` tem `QComboBox` para grupos fixos (Geral, Trabalho, etc).<br>
(&emsp;) A barra de filtro tem ícone 🔍 e `clearButtonEnabled`.<br>
(&emsp;) O `RepositorioContatos` herda de `QWidget`.<br>
(&emsp;) `LinhaContato` usa `QGridLayout` para organizar elementos.<br>
(&emsp;) `JanelaDetalhe` tem tamanho fixo 400x300.<br>
(&emsp;) Há 6 grupos fixos no `QComboBox` do diálogo.<br>
(&emsp;) A toolbar tem botão "Buscar".<br>
(&emsp;) Filtro de texto busca em `nome`, `email`, `telefone` e `grupo`.<br>
(&emsp;) `Ctrl+N` e `Delete` têm atalhos globais via `keyPressEvent`.<br>
(&emsp;) `_recarregar` preserva seleção do combo de grupos.<br>
(&emsp;) Seleção múltipla usa `set[int]` para armazenar IDs.<br>
(&emsp;) `closeEvent` confirma fechamento com botão padrão `No`.<br>
(&emsp;) Todos os contatos demo são favoritos (`favorito=True`).<br>
(&emsp;) `_filtrar_texto` renderiza apenas contatos do grupo atual.<br>
(&emsp;) `LinhaContato` emite selecionado ao checkar `QCheckBox`.<br>
(&emsp;) `Statusbar` tem 3 widgets permanentes.<br>
(&emsp;) `_selecionar_todos` marca apenas contatos filtrados.<br>
(&emsp;) `Contato._next_id` usa contador estático `_counter`.<br>
(&emsp;) `_renderizar` adiciona `QLabel` "Nenhum contato encontrado" se vazio.<br>
(&emsp;) `DialogoContato` valida nome e email como obrigatórios.<br>
(&emsp;) `_toggle_selecao` usa `discard/add` no `set _selecionados`.<br>
(&emsp;) `repo.alterado` conecta a `_recarregar` na inicialização.<br>
(&emsp;) `buscar()` diferencia maiúsculas/minúsculas nos termos.<br>
(&emsp;) `JanelaDetalhe` emite `editar_solicitado` ao clicar "Ver".<br>
(&emsp;) `_remover_selecionados` chama `repo.remover` com lista vazia.<br>
(&emsp;) `_editar_selecionado` permite editar múltiplos contatos.<br>
(&emsp;) `keyPressEvent` chama `super()` apenas para `Escape`.<br>

## 5

```python
import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QLineEdit, QCheckBox, QPushButton, 
    QVBoxLayout, QWidget, QMessageBox)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exemplo 1 - Sinais, Slots, Eventos e Widgets")
        self.setGeometry(100, 100, 420, 280)
        
        central = QWidget()
        self.setCentralWidget(central)
        
        layout = QVBoxLayout(central)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)
        
        self.lbl_nome = QLabel("Nome completo:")
        self.line_nome = QLineEdit()
        self.line_nome.setPlaceholderText("Digite seu nome...")
        
        self.chk_termos = QCheckBox("Aceito os termos de uso e privacidade")
        
        self.btn_enviar = QPushButton("Enviar dados")
        self.btn_enviar.setEnabled(False)  # inicia desabilitado
        
        self.lbl_resultado = QLabel("Resultado aparecerá aqui")
        self.lbl_resultado.setStyleSheet("font-style: italic; color: #555;")
        
        layout.addWidget(self.lbl_nome)
        layout.addWidget(self.line_nome)
        layout.addWidget(self.chk_termos)
        layout.addWidget(self.btn_enviar)
        layout.addWidget(self.lbl_resultado)
        layout.addStretch()
        
        
        self.line_nome.textChanged.connect(self.on_nome_alterado)
        self.chk_termos.toggled.connect(self.on_termos_alterado)
        self.btn_enviar.clicked.connect(self.on_enviar_clicado)
        
        
        self.line_nome.returnPressed.connect(self.on_enviar_clicado)
    
    def on_nome_alterado(self, texto: str):
        self.btn_enviar.setEnabled(bool(texto.strip()))
    
    def on_termos_alterado(self, marcado: bool):
        if not marcado:
            self.lbl_resultado.setText("⚠️ Você precisa aceitar os termos")
            self.lbl_resultado.setStyleSheet("color: red;")
        else:
            self.lbl_resultado.setText("✅ Termos aceitos")
            self.lbl_resultado.setStyleSheet("color: green;")
    
    def on_enviar_clicado(self):
        nome = self.line_nome.text().strip()
        if not nome:
            return
        if self.chk_termos.isChecked():
            self.lbl_resultado.setText(f"✅ Dados enviados com sucesso para: {nome}")
            self.lbl_resultado.setStyleSheet("color: darkgreen; font-weight: bold;")
            
            self.line_nome.clear()
            self.chk_termos.setChecked(False)
            self.btn_enviar.setEnabled(False)
        else:
            QMessageBox.warning(self, "Aviso", "Você deve aceitar os termos antes de enviar.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = MainWindow()
    janela.show()
    sys.exit(app.exec())
```

(&emsp;) O título da janela principal é definido como "Exemplo 1 - Sinais, Slots, Eventos e Widgets".<br>
(&emsp;) O código utiliza o gerenciador de layout `QVBoxLayout` para organizar os widgets verticalmente.<br>
(&emsp;) Existe um widget do tipo `QLineEdit` que exibe o texto de sugestão (placeholder) "Digite seu nome...".<br>
(&emsp;) O botão "Enviar dados" (`btn_enviar`) inicia o programa em um estado desabilitado.<br>
(&emsp;) O programa utiliza a classe `QMainWindow` como base para a criação da janela principal.<br>
(&emsp;) O rótulo inicial de resultado (`lbl_resultado`) exibe o texto "Aguardando envio..." ao iniciar o programa.<br>
(&emsp;) O layout principal possui margens externas configuradas para o valor de 0 em todos os lados.<br>
(&emsp;) A janela é configurada para abrir exatamente no centro da tela através do método `setGeometry`.<br>
(&emsp;) O widget `QCheckBox` é criado com o texto "Li e concordo com as regras do sistema".<br>
(&emsp;) O código importa a classe `QGridLayout` para organizar os componentes em uma grade de linhas e colunas.<br>
(&emsp;) Ao desmarcar a caixa de seleção de termos, a cor do texto do rótulo de resultado muda para vermelho.<br>
(&emsp;) O método `on_nome_alterado` habilita o botão de envio somente se o texto digitado (após remover espaços) não estiver vazio.<br>
(&emsp;) O código aplica um estilo `CSS` (*setStyleSheet*) para que o rótulo de resultado apareça inicialmente em itálico.<br>
(&emsp;) O método `on_enviar_clicado` limpa o conteúdo do campo de texto (line_nome) após um envio bem-sucedido.<br>
(&emsp;) Existe uma conexão de sinal que permite disparar a ação de envio ao pressionar a tecla "Enter" dentro do campo de nome.<br>
(&emsp;) O sinal `toggled` do `QCheckBox` está conectado diretamente ao método `on_enviar_clicado`.<br>
(&emsp;) Quando os dados são enviados com sucesso, a cor do texto do resultado é alterada para azul (blue).<br>
(&emsp;) O método `on_termos_alterado` recebe um argumento do tipo `string` contendo o texto do checkbox.<br>
(&emsp;) O botão de envio torna-se habilitado automaticamente assim que o checkbox de termos é marcado, independente do nome.<br>
(&emsp;) O comando `layout.addStretch()` é usado no início do layout para empurrar todos os widgets para a parte inferior da janela.<br>
(&emsp;) Se o usuário clicar no botão "Enviar dados" (através de atalhos de teclado, por exemplo) com o checkbox desmarcado, um QMessageBox de aviso será exibido.<br>
(&emsp;) O método `on_enviar_clicado` possui uma guarda (verificação) que interrompe a execução se a variável nome estiver vazia após o `strip()`.<br>
(&emsp;) Após um envio bem-sucedido, a caixa de seleção de termos (`chk_termos`) volta para o estado desmarcado programaticamente.<br>
(&emsp;) A variável central do tipo `QWidget` é essencial pois `QMainWindow` exige que layouts sejam definidos em um widget central e não diretamente na janela.<br>
(&emsp;) O uso de `sys.exit(app.exec())` garante que o Python encerre o processo corretamente quando o loop de eventos da interface gráfica for finalizado.<br>
(&emsp;) O método `on_nome_alterado` utiliza o sinal `editingFinished` para validar o nome apenas quando o usuário sai do campo.<br>
(&emsp;) A lógica do código impede que o usuário digite números no campo line_nome, aceitando apenas caracteres alfabéticos.<br>
(&emsp;) O `QMessageBox` utilizado no código é do tipo informativo (information) e possui apenas um botão de "Cancelar".<br>
(&emsp;) A folha de estilo (*stylesheet*) aplicada no sucesso do envio define a fonte como negrito através da propriedade `font-decoration: bold;`.<br>
(&emsp;) O código utiliza herança múltipla para que a classe `MainWindow` herde simultaneamente de `QMainWindow` e `QVBoxLayout`.<br>

## 6

```python
import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout,
    QLabel, QLineEdit, QCheckBox, QPushButton, QToolBar, QStatusBar, QDialog, 
    QMessageBox)
from PySide6.QtGui import QAction


class ConfigDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Configurações Avançadas")
        self.resize(420, 300)
        layout = QVBoxLayout(self)
        
        layout.addWidget(QLabel("Preferências do sistema:"))
        
        self.chk_email = QCheckBox("Enviar relatório por e-mail")
        self.chk_email.setChecked(True)
        layout.addWidget(self.chk_email)
        
        self.chk_backup = QCheckBox("Backup diário automático")
        layout.addWidget(self.chk_backup)
        
        self.txt_pasta = QLineEdit("/home/usuario/relatorios")
        layout.addWidget(QLabel("Pasta de relatórios:"))
        layout.addWidget(self.txt_pasta)
        
        btn = QPushButton("Aplicar todas as configurações")
        btn.clicked.connect(self.accept)
        layout.addWidget(btn)


class JanelaRelatorio(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Relatório Completo - Março 2026")
        self.resize(620, 420)
        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)
        layout.addWidget(QLabel("📊 Resumo de vendas\n\nTotal: R$ 48.920,00\nClientes novos: 14"))
        layout.addStretch()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exemplo 5 - Sistema Completo (mais complexo)")
        self.setGeometry(80, 80, 820, 560)
        
        
        menubar = self.menuBar()
        menu_arquivo = menubar.addMenu("Arquivo")
        menu_arquivo.addAction("Novo cadastro").triggered.connect(self.novo_cadastro)
        menu_arquivo.addAction("Salvar tudo").triggered.connect(self.salvar_tudo)
        menu_arquivo.addSeparator()
        menu_arquivo.addAction("Sair").triggered.connect(self.close)
        
        menu_relatorios = menubar.addMenu("Relatórios")
        menu_relatorios.addAction("Gerar relatório mensal").triggered.connect(self.abrir_relatorio)
        
        
        toolbar = QToolBar("Ações rápidas")
        self.addToolBar(toolbar)
        toolbar.addAction("Novo").triggered.connect(self.novo_cadastro)
        toolbar.addAction("Relatório").triggered.connect(self.abrir_relatorio)
        
        self.setStatusBar(QStatusBar())
        self.statusBar().showMessage("Sistema de Gestão v2.1 - Tudo pronto")
        
        
        central = QWidget()
        self.setCentralWidget(central)
        layout_principal = QVBoxLayout(central)
        
        
        cabecalho = QHBoxLayout()
        cabecalho.addWidget(QLabel("👤 Gestão de Clientes"))
        cabecalho.addStretch()
        layout_principal.addLayout(cabecalho)
        
        
        grid = QGridLayout()
        grid.setSpacing(12)
        
        grid.addWidget(QLabel("Nome:"), 0, 0)
        self.txt_nome = QLineEdit()
        grid.addWidget(self.txt_nome, 0, 1)
        
        grid.addWidget(QLabel("E-mail:"), 1, 0)
        self.txt_email = QLineEdit()
        grid.addWidget(self.txt_email, 1, 1)
        
        grid.addWidget(QLabel("Telefone:"), 2, 0)
        self.txt_telefone = QLineEdit()
        grid.addWidget(self.txt_telefone, 2, 1)
        
        self.chk_ativo = QCheckBox("Cliente ativo no sistema")
        grid.addWidget(self.chk_ativo, 3, 0, 1, 2)
        
        layout_principal.addLayout(grid)
        
        
        hbox_acoes = QHBoxLayout()
        btn_salvar = QPushButton("💾 Salvar Cliente")
        btn_salvar.clicked.connect(self.salvar_cliente)
        hbox_acoes.addWidget(btn_salvar)
        
        btn_config = QPushButton("⚙️ Configurações")
        btn_config.clicked.connect(self.abrir_configuracoes)
        hbox_acoes.addWidget(btn_config)
        
        btn_relatorio = QPushButton("📈 Gerar Relatório")
        btn_relatorio.clicked.connect(self.abrir_relatorio)
        hbox_acoes.addWidget(btn_relatorio)
        
        layout_principal.addLayout(hbox_acoes)
        
        
        self.lbl_feedback = QLabel("Nenhum cliente selecionado ainda")
        self.lbl_feedback.setStyleSheet("background: #f0f0f0; padding: 8px;")
        layout_principal.addWidget(self.lbl_feedback)
        
        
        self.txt_nome.textChanged.connect(self.atualizar_feedback)
        self.chk_ativo.toggled.connect(self.on_status_cliente)
        
        
        self.txt_email.mouseDoubleClickEvent = self.limpar_formulario
    
    
    def atualizar_feedback(self, texto):
        self.lbl_feedback.setText(f"Digitando nome: {texto}")
    
    
    def on_status_cliente(self, ativo):
        self.statusBar().showMessage(f"Cliente agora está {'ATIVO' if ativo else 'INATIVO'}")
    
    def novo_cadastro(self):
        self.txt_nome.clear()
        self.txt_email.clear()
        self.txt_telefone.clear()
        self.chk_ativo.setChecked(True)
        self.lbl_feedback.setText("Novo cadastro iniciado")
    
    def salvar_cliente(self):
        if not self.txt_nome.text():
            QMessageBox.critical(self, "Erro", "Nome é obrigatório!")
            return
        QMessageBox.information(self, "Sucesso", f"Cliente {self.txt_nome.text()} cadastrado com sucesso!")
    
    def salvar_tudo(self):
        QMessageBox.information(self, "Backup", "Todos os dados foram salvos com sucesso.")
    
    def abrir_configuracoes(self):
        dialog = ConfigDialog(self)
        dialog.exec()
    
    def abrir_relatorio(self):
        self.janela_rel = JanelaRelatorio()
        self.janela_rel.show()
    
    def limpar_formulario(self, event):
        """Evento de duplo-clique no campo e-mail."""
        self.txt_nome.clear()
        self.txt_email.clear()
        self.lbl_feedback.setText("Formulário limpo por duplo-clique")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = MainWindow()
    janela.show()
    sys.exit(app.exec())
```

(&emsp;) A janela principal possui uma barra de ferramentas chamada "Ações rápidas".<br>
(&emsp;) O diálogo de configurações (`ConfigDialog`) já vem com uma sugestão de caminho de pasta preenchida no `QLineEdit`.<br>
(&emsp;) Existe um menu chamado "Relatórios" que contém a opção "Gerar relatório mensal".<br>
(&emsp;) O campo de texto para o telefone está posicionado na linha 2 do `QGridLayout`.<br>
(&emsp;) O rótulo de feedback (`lbl_feedback`) possui uma cor de fundo cinza claro (`#f0f0f0`) definida via folha de estilo.<br>
(&emsp;) O título da janela de relatório é "Relatório Anual - 2026".<br>
(&emsp;) O botão de salvar cliente possui apenas texto, sem nenhum emoji ou ícone.<br>
(&emsp;) A largura inicial da janela principal é de 1024 pixels.<br>
(&emsp;) O checkbox "Backup diário automático" inicia o programa já marcado (`Checked`).<br>
(&emsp;) O código utiliza um `QComboBox` para o usuário selecionar o estado civil do cliente.<br>
(&emsp;) O método `atualizar_feedback` é disparado toda vez que o usuário digita ou apaga uma letra no campo de nome.<br>
(&emsp;) Ao alterar o estado do checkbox "Cliente ativo", uma mensagem em letras maiúsculas (ATIVO ou INATIVO) aparece na barra de status.<br>
(&emsp;) O método `salvar_cliente` exibe uma mensagem de erro do tipo `critical` caso o campo de nome esteja vazio.<br>
(&emsp;) A função `novo_cadastro` limpa três campos de texto e marca o checkbox de cliente ativo.<br>
(&emsp;) Existe um separador visual no menu "Arquivo" entre as opções de salvar e sair.<br>
(&emsp;) O botão "Gerar Relatório" abre o diálogo de configurações antes de mostrar o relatório.<br>
(&emsp;) O método `salvar_tudo` fecha a aplicação automaticamente após exibir a mensagem de sucesso.<br>
(&emsp;) O sinal `textChanged` do campo de e-mail está conectado à função `limpar_formulario`.<br>
(&emsp;) A barra de status exibe a versão do sistema como "v1.0" no momento em que o programa abre.<br>
(&emsp;) O diálogo `ConfigDialog` permite que o usuário redimensione a janela livremente para qualquer tamanho.<br>
(&emsp;) O código sobrescreve o comportamento padrão do campo de e-mail para que um duplo-clique do mouse limpe o formulário.<br>
(&emsp;) A classe `JanelaRelatorio` herda de `QMainWindow`, o que permite que ela tenha sua própria estrutura independente de menus e barras laterais se necessário.<br>
(&emsp;) Na função `abrir_relatorio`, a nova janela é atribuída a `self.janela_rel` para garantir que a variável não saia de escopo e a janela não feche sozinha.<br>
(&emsp;) O método `self.close` é chamado diretamente pelo sinal `triggered` da ação "Sair", sem a necessidade de criar uma função intermediária.<br>
(&emsp;) O `QGridLayout` utiliza um espaçamento (`Spacing`) de 12 pixels entre os widgets para evitar que os campos fiquem muito colados.<br>
(&emsp;) O evento de duplo-clique no campo de e-mail (`mouseDoubleClickEvent`) só funciona se o usuário clicar com o botão direito.<br>
(&emsp;) O método `dialog.exec()` é assíncrono, permitindo que o usuário continue preenchendo o nome enquanto o diálogo de configurações está aberto.<br>
(&emsp;) No menu "Arquivo", a ação "Novo cadastro" é criada usando a classe `QAction` instanciada separadamente em uma variável.<br>
(&emsp;) A janela de relatório exibe o valor total de vendas como um número inteiro, sem formatação de moeda (R$).<br>
(&emsp;) O layout cabecalho (`QHBoxLayout`) coloca o rótulo "Gestão de Clientes" obrigatoriamente no lado direito da janela.<br>

## Gabarito

<details>
  <summary>Respostas</summary>
  <p><b>1</b>: V V V V V F F F F F V V V V V F F F F F V V V V V F F F F F</p>
  <p><b>2</b>: V V V V V F F F F F V V V V V F F F F F V V V V V F F F F F</p>
  <p><b>3</b>: V V V V V F F F F F V V V V V F F F F F V V V V V F F F F F</p>
  <p><b>4</b>: V V V V V F F F F F V V V V V F F F F F V V V V V F F F F F</p>
  <p><b>5</b>: V V V V V F F F F F V V V V V F F F F F V V V V V F F F F F</p>
  <p><b>6</b>: V V V V V F F F F F V V V V V F F F F F V V V V V F F F F F</p>
</details>