# Aula 05

## Manipulação de arquivos em Python

Um objeto de arquivo em Python, de acordo com [seu glossário](https://docs.python.org/3/glossary.html#term-file-object), consiste em um objeto expondo uma **API orientada a arquivos** (com métodos como `read()` ou `write()`).

Dependendo de como foi criado o objeto de arquivo pode mediar o acesso a um arquivo real no disco ou a outro tipo de armazenamento ou dispositivo de comunicação (e.g., *input/output* padrão, *in-memory buffers*, *sockets*, *pipers*, etc.).

Existem três categorias de objetos de arquivo:

- [Arquivos binários brutos](https://docs.python.org/3/glossary.html#term-binary-file).
- Arquivos binários em *buffer*.
- [Arquivo de texto](https://docs.python.org/3/glossary.html#term-text-file)
  -  Um objeto de arquivo capaz de ler e escrever objetos `str`. 
  -  Frequentemente, um arquivo de texto acessa um fluxo de dados orientado a bytes (*byte-oriented datastream*) e lida com a codificação do texto automaticamente.
  
Suas interfaces são definidas no módulo [`io`](https://docs.python.org/3/library/io.html#module-io). A forma canônica de criar um objeto de arquivo é usando a função nativa [`open()`](https://docs.python.org/3/builtins/functions.html#open).

## A função [`open()`](https://docs.python.org/3/builtins/functions.html#open)

`open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)`

Essa função abre um arquivo e retorna o objeto de arquivo correspondente.

Os dois principais parâmetros são:

- `file` (obrigatório): costuma ser um objeto [`path-like`](https://docs.python.org/3/glossary.html#term-path-like-object) contendo o caminho até o arquivo.
- `mode` (opcional): se refere ao modo de acesso. A seguir, alguns modos de acesso:
  - `'r'`: *read* / leitura (*default*).
  - `'w'`: *write* / escrita -> sobrescreve ("trunca") o arquivo, ou cria um novo.
  - `'x'`: *exclusive*, exclusivo para criação, falhando se o arquivo já existe.
  - `'a'`: *append*, para escrita ao fim do arquivo se ele existir. Se o arquivo não existe, ele é criado.
  - `'b'`: modo binário.
  - `'t'`: modo textual (*default*).
  - `'+'`: *update* / atualização (leitura e escrita).
  - **Combinações possíveis:** 
    - `'r'`/`'rt'`;
    - `'rb'`;
    - `'r+'`/`'r+t'`;
    - `'rb+'`/`'r+b'`;
    - `'w'`/`'wt'`;
    - `'wb'`;
    - `'w+'`/`'w+t'`;
    - `'wb+'`/`'w+b'`;
    - `'a'`/`'at'`;
    - `'ab'`;
    - `'a+'`/`'a+t'`;
    - `'ab+'`/`'a+b'`;
    - `'x'`/`'xt'`;
    - `'xb'`;
    - `'x+'`/`'x+t'`;
    - `'xb+'`/`'x+b'`.

A hierarquia das classes, no módulo `io` é a seguinte:

|  | **Herda de** | **Stub Methods** | **Mixin Methods** e **Properties** |
|---|---|---|---|
| [`IOBase`](https://docs.python.org/3/library/io.html#io.IOBase) |  | `fileno`, `seek` e `truncate` | `close`, `closed`, `__enter__`, `__exit__`, `flush`, `isatty`, `__iter__`, `__next__`, `readable`, `readline`, `readlines`, `seekable`, `tell`, `writable` e `writelines` |
| [`RawIOBase`](https://docs.python.org/3/library/io.html#io.RawIOBase) | [`IOBase`](https://docs.python.org/3/library/io.html#io.IOBase) |  `readinto` e `write` | Métodos herdados, `read` e `readall` |
| [`BufferedIOBase`](https://docs.python.org/3/library/io.html#io.BufferedIOBase) | [`IOBase`](https://docs.python.org/3/library/io.html#io.IOBase) | `detach`, `read`, `read1` e `write` | Métodos herdados, `readinto` e `readinto1` |
| [`TextIOBase`](https://docs.python.org/3/library/io.html#io.TextIOBase) | [`IOBase`](https://docs.python.org/3/library/io.html#io.IOBase) | `detach`, `read`, `readline` e `write` | Métodos herdados, `encoding`, `errors` e `newlines` | 

### Abrindo arquivo existente com o modo de acesso `read`

Junto com o método `open()`, é interessante sempre escrever logo o `.close()`, para evitar problemas. Caso a execução seja interrompida, ou finalizada normalmente, sem que o arquivo seja fechado, é possível que você tenha problemas para acessá-lo, mesmo com outro programa, como o bloco de notas. [Exemplo](./exemplos/exemplo01.py):

```python
arquivo = open("./AULAS/05/exemplos/teste.txt", "r")

print(arquivo.readable())  # imprimindo a verificação se o arquivo pode ser lido
print(arquivo.read())      # imprimindo o arquivo

arquivo.close()
```

Existe outra forma mais "cômoda" de lidar com abertura e fechamento de arquivos: `with open()`. Neste caso, o próprio Python garantirá o fechamento adequado do arquivo. Vejamos um [exemplo](exemplos/exemplo02.py):

```python
with open("./AULAS/05/exemplos/teste.txt", "r") as arquivo:
    print(arquivo.readline())
    print(arquivo.readline())
    print(arquivo.readline())
```

No exemplo anterior `readline()` lê uma linha e deixa o `cursor` na linha seguinte. Portanto, uma sequência de `readline()` vai retornar sempre a linha seguinte. Com o `print()`, a leitura de cada linha é impressa. Como cada linha do arquivo que está sendo lido termina com `\n` (quebra de linha) o resultado de cada `readline()` vai ter a seguir uma linha em branco.

A função `readlines()` retorna uma lista, onde cada elemento da lista é o conteúdo de uma linha. Essa lista está sendo armazenada na variável lista. A partir daí podemos manipular a lista. Perceba que manipulando a lista, mesmo que apagando elementos, não vai afetar o arquivo. Exemplo:

```python
with open("./AULAS/05/exemplos/teste.txt", "r") as arquivo:
    lista = arquivo.readlines()
    print(lista)
```

**Curiosidade:** imprima a lista usando `for` e veja a diferença.

### Abrindo um arquivo existente com o modo de acesso `append`.

Esse modo permite acrescentar conteúdo ao arquivo sem truncá-lo. Quando o arquivo é aberto em modo `'a'` a nova escrita vai iniciar no espaço seguinte ao último já existente. No nosso exemplo, em `teste.txt`, temos como último elemento a palavra Matlab. Com o `append`, a nova escrita começa colado ao Matlab. Logo, se acrescentamos o `\n`, vai haver primeiro uma quebra de linha. O C# é escrito logo após a quebra de linha. [Exemplo](exemplos/exemplo04.py):

```python
with open(".AULAS/05/exemplos/teste.txt", "a") as arquivo:
    arquivo.write("COBOL")
    arquivo.write("\nC#")
```

### Abrindo um arquivo existente com o modo de acesso `write`.

O modo `'w'` vai truncar o arquivo, caso ele exista, ou seja, vai apagar o que já estava lá. Se o arquivo não existir, ele vai ser criado. [Exemplo](exemplos/exemplo05.py) de criação:

```python
with open("./AULAS/05/exemplos/teste2.txt", "w") as arquivo:
    arquivo.write("Portugol\n")
    arquivo.write("ADA\n")
    arquivo.write("C#")
```

[Exemplo](exemplos/exemplo06.py) de truncamento:

```python
with open("./AULAS/05/exemplos/teste2.txt", "w") as arquivo:
    arquivo.write("DART\n")
    arquivo.write("Ruby\n")
    arquivo.write("Assembly")
    arquivo.write("Haskell")
```

### Remoção de arquivos

A remoção de arquivos pode ser feita com a importação do módulo `os` (de operating system, ou sistema operacional). Esse módulo provê uma interface para funcionalidades dependentes do sistema operacional. Exemplo:

```python
import os

with open("./AULAS/05/exemplos/teste3.txt", "w") as arquivo:
    arquivo.write("Cubo Mágico")

if os.path.exists("teste3.txt"):
    os.remove("teste3.txt")
else:
    print("Arquivo não existe")
```

### Diretórios / Pastas

Da mesma forma, ou seja, com o uso do módulo `os`, é possível criar e remover pastas. Entretanto, a remoção só é possível se a pasta estiver vazia.

```python
import os

os.mkdir("./AULAS/05/exemplos/exemplo")
os.rmdir("./AULAS/05/exemplos")
```

## Exercícios

### Fáceis

1. Crie um script que abra um arquivo de texto chamado "exemplo.txt" e imprima todo o seu conteúdo na tela.
2. Escreva um programa que crie um novo arquivo chamado "saida.txt" e escreva a string "Olá, mundo!" nele.
3. Abra o arquivo "exemplo.txt" e imprima apenas a primeira linha do arquivo.
4. Leia todas as linhas de "exemplo.txt" em uma lista e imprima o número total de linhas.
5. Conte o número de palavras no arquivo "exemplo.txt" (considere que as palavras são separadas por espaços).
6. Copie o conteúdo inteiro de "entrada.txt" para um novo arquivo chamado "copia.txt".
7. Abra "exemplo.txt" em modo de append e adicione a linha "Nova linha adicionada." no final.
8. Verifique se o arquivo "exemplo.txt" existe antes de tentar abri-lo e imprima uma mensagem apropriada.
9. Crie um arquivo "numeros.txt" e escreva os números de 1 a 10, um por linha.
10. Leia o arquivo "exemplo.txt" e imprima cada linha em maiúsculas.
11. Substitua todas as ocorrências da palavra "Python" por "Java" no arquivo "exemplo.txt" e salve em um novo arquivo.
12. Leia "exemplo.txt", divida o texto em palavras e imprima a lista de palavras.
13. Conte quantas vezes a letra 'a' aparece no arquivo "exemplo.txt" (case-insensitive).
14. Inverta a ordem das linhas de "exemplo.txt" e escreva o resultado em "invertido.txt".
15. Leia as linhas de "exemplo.txt", ordene-as alfabeticamente e escreva em "ordenado.txt".
16. Encontre e imprima a linha mais longa (em caracteres) do arquivo "exemplo.txt".
17. Remova todas as linhas vazias de "exemplo.txt" e salve o resultado em "limpo.txt".
18. Use um gerenciador de contexto (with) para abrir "exemplo.txt" e imprimir seu conteúdo.
19. Crie um arquivo "vogais.txt" escrevendo apenas as vogais encontradas em "exemplo.txt".
20. Leia "exemplo.txt" e imprima o tamanho total do arquivo em bytes.

### Médias

21. Leia dois arquivos de texto ("arquivo1.txt" e "arquivo2.txt") e concatene seu conteúdo em um terceiro arquivo "uniao.txt".
22. Procure por uma palavra específica (ex: "erro") em "log.txt" e imprima as linhas que a contêm.
23. Trate um erro de arquivo não encontrado ao tentar abrir "nao_existe.txt" e imprima uma mensagem de erro personalizada.
24. Leia "exemplo.txt" com codificação UTF-8 e converta todo o texto para minúsculas, salvando em "minusculo.txt".
25. Crie um dicionário de frequência de palavras em "exemplo.txt" e imprima as 5 palavras mais comuns.
26. Numere as linhas de "exemplo.txt" (ex: "1: linha um") e escreva em "numerado.txt".
27. Compare dois arquivos linha por linha e imprima as diferenças em "diferencas.txt".
28. Gere um backup de "exemplo.txt" renomeando-o para "exemplo_backup.txt" se o original existir.
29. Leia "exemplo.txt", remova linhas que contenham uma palavra específica (ex: "ignore") e salve o filtro em "filtrado.txt".
30. Crie um arquivo "resumo.txt" que contenha o número de linhas, palavras e caracteres de "exemplo.txt".
31. Divida "exemplo.txt" em parágrafos (separados por linhas vazias) e salve cada parágrafo em um arquivo separado (ex: para1.txt, para2.txt).
32. Encontre todas as linhas que são palíndromos em "exemplo.txt" e liste-as.
33. Substitua múltiplas palavras em "exemplo.txt" usando um dicionário de substituições e salve o resultado.
34. Leia "exemplo.txt" e "referencia.txt", encontre linhas comuns e escreva em "comuns.txt".
35. Trate exceções ao escrever em um arquivo que está sendo lido simultaneamente (use try-except).
36. Crie um script que processe todos os arquivos .txt em um diretório e conte o total de palavras em todos eles.
37. Adicione timestamps (data/hora atual) no início de cada linha ao ler e reescrever "exemplo.txt".
38. Valide se "exemplo.txt" tem exatamente 10 linhas; se não, adicione linhas vazias até atingir o número.
39. Extraia apenas os números de "exemplo.txt" (usando expressões regulares simples) e salve em "numeros_extraidos.txt".
40. Crie um arquivo "estatisticas.txt" com a média de comprimento das linhas de "exemplo.txt".

### Difíceis

Para a resolução das questões a seguir, você precisa criar arquivos que se encaixem nas descrições.

1.  Processe um arquivo grande ("log_grande.txt") em chunks de 1024 bytes, contando erros (linhas com "ERROR") sem carregar tudo na memória.
2.  Use expressões regulares para extrair e-mails de "emails.txt" e valide-os salvando apenas os válidos em "validos.txt".
3.  Edite "exemplo.txt" in-place (sem criar cópia), removendo linhas duplicadas consecutivas.
4.  *Parse* um arquivo de configuração simples (formato chave=valor) em "config.txt" e crie um dicionário para usá-lo em outro arquivo.
5.  Compare a similaridade entre dois arquivos grandes usando um algoritmo simples de dif (ex: contagem de palavras comuns) e gere um relatório.
6.  Gere um relatório consolidado de múltiplos arquivos de log ("log1.txt" a "log5.txt"), somando contagens de eventos por categoria.
7.  Implemente uma busca e substituição condicional em "exemplo.txt": substitua "old" por "new" apenas se a linha contiver "if".
8.  Crie um script que leia "arvore.txt" (formato hierárquico indentado), construa uma árvore de dados e salve uma versão JSON-like em texto.
9.  Otimize a leitura de "arquivo_enorme.txt" para buscar uma substring em tempo O(1) aproximado, usando índices de linhas.
10. Integre manipulação de arquivos com uma estrutura de dados: leia "transacoes.txt", processe transações em uma lista de dicionários, valide saldos e gere um arquivo de auditoria com discrepâncias.