# Exercícios para a AV1

## 1

Desenhe e explique a arquitetura mínima (classes e responsabilidades) de uma aplicação Tkinter orientada a objetos que tenha: janela principal, uma barra de ferramentas com botões, área de conteúdo que pode alternar entre duas telas (por exemplo “Lista” e “Detalhe”) e uma barra de status. Explique como você compartilharia estado entre as telas e como garantiria separação de responsabilidades.

## 2

Explique, com um pequeno esboço de código, a diferença prática entre usar um `Button(..., command=...)` e usar `widget.bind('<Button-1>', ...)` para reagir a cliques. Em que situações cada abordagem é mais apropriada? Quais cuidados tomar se o mesmo widget precisa reagir a diferentes tipos de clique?

## 3

Proponha três estratégias distintas para aplicar estilos consistentes (fonte, espaçamento, cores) em uma aplicação Tkinter que deve rodar em Windows e Linux, usando `ttk` quando possível. Explique vantagens e desvantagens de cada estratégia.

## 4

Você precisa construir um pequeno editor de texto com área principal (Text), barra de rolagem e indicador de progresso que mostra proporção do texto selecionado. Escreva o esqueleto (pseudo-código ou código curto) e explique como irá conectar `Text`, `Scrollbar` e `Progressbar` de forma reativa (sem polling constante).

## 5

Descreva duas situações em que usar `place` é a melhor escolha e duas em que `grid` ou `pack` são melhores. Para cada situação explique por que a escolha é justificada em termos de manutenção e adaptabilidade da interface.

## 6

Em termos de usabilidade e validação, explique como você implementaria validação em um campo `Entry` para aceitar apenas números dentro de um intervalo. Discuta abordagens com `validate`/`validatecommand`, com `StringVar` + trace, e com checagem no momento do envio (por exemplo, ao clicar “Salvar”). Compare robustez e UX.

## 7

Imagine que você precisa exibir uma hierarquia de arquivos com possibilidade de colapsar/expandir e múltiplas colunas de informação (nome, tamanho, tipo). Justifique por que escolher `Treeview` em vez de `Listbox`, e descreva (em alto nível) como trataria seleção múltipla, ordenação por coluna e atualização incremental dos dados.

## 8

Explique o papel de `mainloop()` em um aplicativo Tkinter. Considere também: o que acontece se você chamar funções longas diretamente no callback da GUI e quais padrões (ex.: `after`, threads, processos, jobs) você usaria para manter a interface responsiva.

## 9

Discuta o uso de `StringVar`, `IntVar` e outros `Variable` em termos de design: quando é vantajoso usá-los (ex.: ligação direta a widgets), quando evitá-los (por ex., muitos objetos ligados causando complexidade) e quais alternativas arquiteturais existem para compartilhar estado entre widgets (ex.: modelo central, sinais customizados).

## 10

Explique, com diagrama simples ou descrição, como implementar a alternância entre frames (“trocar telas”) em uma aplicação POO (por exemplo, usando um gerenciador que mantém instâncias de frames). Como você trataria inicialização tardia (lazy) de telas para reduzir memória/tempo de startup?

## 11

Considere o trecho abaixo:

```python
import tkinter as tk
root = tk.Tk()
btn = tk.Button(root, text="Clique", command=lambda: print("oi"))
btn.pack()
# linha X
```

Qual das alternativas em **linha X** fará a janela aparecer e responder a eventos de usuário?

A. `root.update()`

B. `root.mainloop()`

C. `root.start()`

D. `tk.mainloop(root)`

E. `root.run()`

## 12

Você criou um `Frame` chamado `f` e, dentro dele, um `Label`. Qual das seguintes situações **causa normalmente um erro** em tempo de execução?

A. Chamou `f.pack()` e depois `Label(f, text="x").grid()` no mesmo `f`.

B. Chamou `Label(f, text="x").pack()` duas vezes no `Label`.

C. Chamou `Label().pack()` sem passar parent.

D. Chamou `grid()` em um widget que já foi `pack()`ado em outro container.

E. Chamou `Label(f, text="x")` e não chamou `pack()`/`grid()` (o Label não aparece).

## 13

Sobre handlers (funções de callback) em Tkinter, qual afirmativa é a **mais precisa**?

A. Uma função passada a `command=` recebe sempre um objeto `event` como primeiro argumento.

B. Uma função usada em `widget.bind('<Key>', handler)` recebe um objeto `event` como argumento; a mesma função passada em `command=` **não** receberá `event`.

C. `command=` e `bind` chamam o mesmo tipo de callback, com assinatura idêntica.

D. Callbacks usados em `command=` devem sempre ser métodos `@staticmethod`.

E. Não há diferença prática entre `command=` e `bind` para eventos de mouse.

## 14

Sobre `place` em Tkinter, qual alternativa descreve corretamente uma característica do `place`?

A. `place` organiza widgets automaticamente em linhas e colunas.

B. `place` só aceita coordenadas relativas (relx/rely).

C. `place` permite posicionamento absoluto (x/y) e relativo (relx/rely), ideal para layouts pixel-perfect.

D. `place` sempre respeita a ordem z-index, não sendo possível controlar sobreposição.

E. `place` é recomendado para todas interfaces responsivas.

## 15

Em um `Canvas`, você cria um retângulo:

```python
c.create_rectangle(0,0,100,100)
c.create_rectangle(50,50,150,150)
```

Qual será a consequência visível imediatamente após chamar esses métodos (assumindo que os elementos são exibidos)?

A. Dois retângulos não se sobrepõem.

B. O segundo retângulo sobrepõe parcialmente o primeiro.

C. Os dois retângulos se mesclam formando um único polígono.

D. O último `create_rectangle` apaga o anterior.

E. Apenas o primeiro retângulo aparece.

## 16

Você deseja que uma chamada ocorra logo após a interface terminar de processar eventos em curso, sem bloquear. Qual método é adequado?

A. Executar a função diretamente no callback (sincrono).

B. `root.after(0, func)` — agenda `func` para logo depois do processamento atual.

C. `root.sleep(0)` — pausa a UI um instante e executa.

D. `root.call_later(func)` — método padrão do Tkinter.

E. `threading.Thread(target=func).run()` — executa na mesma thread.

## 17

Sobre `ttk.Style` e nomes de estilo: se você configurou `Style().configure('My.TButton', padding=10)` e cria `ttk.Button(..., style='TButton')`, qual afirmação é correta?

A. O botão usará `My.TButton` automaticamente.

B. O botão usará as configurações de `TButton`, não de `My.TButton`.

C. O botão levantará exceção por nome de estilo inválido.

D. `ttk` ignora estilos personalizados sempre que `style` é string.

E. O nome `TButton` e `My.TButton` são sinônimos.

## 18

Em relação a `Notebook` (guias), qual comportamento é esperado quando você remove a aba atual e há outras abas ainda existentes?

A. A aplicação fecha automaticamente.

B. O `Notebook` seleciona outra aba (normalmente a próxima ou a anterior) se disponível.

C. O `Notebook` fica sem foco e sem aba selecionada até o usuário clicar.

D. Todas as abas são removidas automaticamente.

E. O `Notebook` lança um erro se a aba removida era a ativa.

## 19

Ao usar `pack()` com vários widgets em um container, os widgets são empilhados na ordem em que \_\_\_\_\_\_\_\_\_\_\_\_ e a propriedade `side='left'` fará com que sejam posicionados \_\_\_\_\_\_\_\_\_\_\_\_.

## 20

Ao precisar de uma lista rolável de textos editáveis e com quebras de linha, é mais apropriado usar o widget `______` em vez de `Listbox`, porque ele permite \_\_\_\_\_\_.

## 21

Um `StringVar` pode ser usado para ligar o conteúdo de um `Entry` a uma variável Python. Se eu quiser reagir imediatamente a cada mudança no conteúdo dessa `StringVar`, eu usaria o mecanismo de callback chamado \_\_\_\_\_\_.

## 22

Para garantir que uma coluna de um `grid` cresça quando a janela for redimensionada, devo usar `grid_columnconfigure(index, weight=______)`, atribuindo um valor \_\_\_\_\_\_.

## 23

Sobre `Treeview`, assinale as corretas:

(&emsp;) `Treeview` pode apresentar colunas multiplas (cabeçalhos).
(&emsp;) `Treeview` é ideal para edição rica de texto com múltiplas linhas por célula.
(&emsp;) `Treeview` suporta seleção de múltiplos itens se `selectmode='extended'`.
(&emsp;) Para atualizar um item do `Treeview` você deve remover e recriar todo o `Treeview`.
(&emsp;) `Treeview` pode exibir hierarquia (nós filhos/filhos de filhos).}

## 24

Qual(is) das alternativas abaixo são aspectos que tornam o uso de POO útil em apps Tkinter? (escolha todas aplicáveis)

(&emsp;) Encapsular um conjunto de widgets e lógica em um `Frame`-classe facilita reuso.
(&emsp;) Classes permitem compartilhar estado sem passar referências entre funções.
(&emsp;) OOP elimina a necessidade de gerenciar callbacks/eventos.
(&emsp;) Usar classes facilita testes unitários e separação de responsabilidades.
(&emsp;) Classes tornam impossível usar `ttk` corretamente.

## 25

Em relação a `Canvas` e coordenadas, assinale a alternativa **incorreta**:

A. O canto superior esquerdo do `Canvas` é normalmente (0,0).

B. Coordenadas podem ser negativas para desenhar fora da área visível.

C. Objetos do `Canvas` mantêm id único retornado por `create_*`.

D. `Canvas` gerencia automaticamente widgets `Entry` embutidos sem `create_window`.

E. É possível transformar/rotacionar objetos do `Canvas` apenas com coordenadas explícitas.

## 26

Sobre `ttk.Combobox` e seleção, qual alternativa é **incorreta**?

A. `Combobox` pode ser configurada como somente leitura (`state='readonly'`).

B. `Combobox.get()` retorna a string atualmente exibida.

C. `Combobox` não permite vincular a um `StringVar`.

D. `Combobox` pode disparar evento `<<ComboboxSelected>>` quando a seleção muda.

E. `Combobox` aceita uma lista de valores no parâmetro `values=`.

## 27

**A**: `Entry` tem a opção `show='*'` que oculta o texto digitado (útil para senhas).

**R**: `Entry` com `show` ativo continua retornando o texto original em `get()`.

A. **A** e **R** são verdadeiros e **R** explica **A**.

B. **A** e **R** são verdadeiros, mas **R** não explica **A**.

C. **A** é verdadeiro e **R** é falso.

D. **A** e **R** são falsos.

## 28

**A**: Ao usar `widget.bind('<Return>', handler)` a função `handler` receberá um argumento `event` com atributos como `x`, `y`, `keysym`.

**R**: Esses atributos permitem, por exemplo, saber qual tecla foi pressionada e a posição do cursor no momento do evento.

A. **A** e **R** são verdadeiros e **R** explica **A**.

B. **A** e **R** são verdadeiros, mas **R** não explica **A**.

C. **A** é verdadeiro e **R** é falso.

D. **A** e **R** são falsos.

## 29

**A**: `ttk.Progressbar` no modo `determinate` aceita chamadas para `step()` e `start()`.

**R**: No modo `indeterminate` a barra mostra progresso baseado em `maximum` e `value` apenas, sem animação.

A. **A** e **R** são verdadeiros e **R** explica **A**.

B. **A** e **R** são verdadeiros, mas **R** não explica **A**.

C. **A** é verdadeiro e **R** é falso.

D. **A** e **R** são falsos.

## 30

**A**: `Frame` é frequentemente usado como contêiner lógico para agrupar widgets e facilitar layout.

**R**: `Frame` herda todas as funcionalidades de entrada de texto de `Text`, portanto pode ser usado como substituto quando precisamos de editor de texto.

A. **A** e **R** são verdadeiros e **R** explica **A**.

B. **A** e **R** são verdadeiros, mas **R** não explica **A**.

C. **A** é verdadeiro e **R** é falso.

D. **A** e **R** são falsos.

## 31

No Tkinter, para associar uma função que recebe o evento quando o usuário pressiona Enter dentro de um `Entry`, costuma-se fazer:

```python
entry.bind('________', handler)
```

## 32

Para criar um `Label` dentro de um `Frame` chamado `f` e garantir que o texto seja cortado (com quebra) automaticamente para caber na largura do `Frame`, usamos `Label(f, text=texto, wraplength=_____)`. Preencha a lacuna com o tipo de valor esperado (ex.: número + unidade).

## 33

A função `after` permite agendar execução futura: `root.after(____, func)` — preencha a lacuna com o tipo de dado que representa o atraso (por exemplo: \_\_\_\_\_\_).

## 34

Para criar uma barra de rolagem vertical e associá-la a um `Text` chamado `tx`, duas chamadas típicas são `scrollbar.config(command=tx.______)` e `tx.config(yscrollcommand=scrollbar.set)`. Preencha a lacuna com o método do `Text`.

## 35

Dado o trecho:

```python
import tkinter as tk
root = tk.Tk()
v = tk.IntVar(value=0)
chk = tk.Checkbutton(root, text='OK', variable=v)
chk.pack()
v.set(1)
print(v.get())
```

Explique qual valor será impresso e por quê. Se o usuário clicar no checkbox depois do `v.set(1)`, o que acontece com `v.get()`?

## 36

Analise:

```python
from tkinter import *
root = Tk()
t = Text(root, height=3, width=20)
t.pack()
t.insert('1.0', 'Linha1\nLinha2\nLinha3')
t.delete('1.0', '1.end')
```

Qual será o conteúdo final do `Text` exibido ao usuário? Justifique o uso dos índices utilizados.

## 37

Considere um `Treeview` com seleção e um código que remove o item selecionado:

```python
sel = tree.selection()
for iid in sel:
    tree.delete(iid)
```

Se o usuário selecionar um nó pai que contém nós filhos, qual será o comportamento do `tree.delete(iid)` quanto aos filhos? Eles são removidos automaticamente? Explique.

## 38

Relacione (coluna A) com (coluna B). Escreva pares, ex.: A1–B3.

Coluna A:
A1. `pack(side='top')`
A2. `grid(row=0, column=1)`
A3. `place(relx=0.5, rely=0.5)`

Coluna B:
B1. Posicionamento relativo ao centro do contêiner (porcentagem).
B2. Posicionamento em células de uma grade.
B3. Empilhamento vertical por ordem de chamada.

## 39

Relacione widget a caso de uso ideal.

Coluna A:
A1. `Canvas`
A2. `Listbox`
A3. `ScrolledText`

Coluna B:
B1. Exibir muitos itens simples e selecionar por índice.
B2. Desenhos, formas, elementos gráficos e widgets embutidos.
B3. Área de texto editável com scroll integrado.

## 40

Ordene as etapas para trocar de tela em uma aplicação POO com múltiplos `Frame` (do mais alto nível ao mais específico):

* A: ocultar frame atual (por exemplo, `pack_forget()` ou `grid_remove()`)
* B: criar novo frame (se ainda não existir)
* C: instanciar gerenciador de telas (container que conhece frames)
* D: empacotar/exibir o novo frame

Forneça a ordem lógica.