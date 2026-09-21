# Aula 06

**Sumário**

- [Aula 06](#aula-06)
  - [JSON](#json)
    - [Principais funções](#principais-funções)
    - [Exemplos](#exemplos)
    - [Exercícios](#exercícios)
      - [Fácil](#fácil)
      - [Médio](#médio)
      - [Difícil](#difícil)
  - [CSV](#csv)
    - [Exemplos](#exemplos-1)
    - [Exercícios](#exercícios-1)
      - [Fáceis](#fáceis)
      - [Médios](#médios)
      - [Difíceis](#difíceis)


## JSON

O módulo [`json`](https://docs.python.org/3.14/library/json.html) é uma ferramenta essencial e nativa do Python, utilizada para converter objetos Python em strings no formato JSON (*JavaScript Object Notation*) e vice-versa. Ele é amplamente usado em APIs web, arquivos de configuração e armazenamento de dados simples.

### Principais funções

Existem dois pares de funções principais que você precisa conhecer. A diferença entre elas é o destino/origem dos dados (memória vs. arquivo).

| **Função** | **Descrição** |
|---|---|
| `json.dump()` | Escreve um objeto Python diretamente em um arquivo JSON. |
| `json.dumps()` | Converte um objeto Python para uma string JSON (*Serialization*) |
| `json.load()` | Lê um arquivo JSON e o converte para um objeto Python. |
| `json.loads()` | Converte uma string JSON de volta para um objeto Python (*Deserialization*). |

A codificação/decodificação obedece à seguinte tabela:

| **Python** | **JSON** |
|---|---|
| dict | object |
| list, tuple | array |
| str | string |
| int, float, int- & float-derived Enums | number |
| True | true |
| False | false |
| None | null |

### Exemplos

- [Exemplo 1](exemplos/exemplo01.py)
    > **Obs.:** Para salvar arquivos `.json` com caracteres especiais (acentos, etc.) é preciso utilizar o parâmetro `ensure_ascii=False` nas chamadas das funções `dump` ou `dumps`.
- [Exemplo 2](exemplos/exemplo02.py)

### Exercícios

#### Fácil

1. Crie um script que abra um arquivo JSON chamado "dados.json" e imprima todo o seu conteúdo formatado.
2. Escreva um programa que crie um novo arquivo JSON chamado "saida.json" com um dicionário simples: {"nome": "João", "idade": 25}.
3. Carregue "dados.json" e imprima o valor da chave "nome" (assumindo que existe).
4. Conte o número total de chaves de nível superior no dicionário raiz de "dados.json".
5. Carregue "dados.json" e imprima todos os valores de uma lista sob a chave "frutas" (assumindo que é uma lista).
6. Copie o conteúdo inteiro de "entrada.json" para um novo arquivo chamado "copia.json".
7. Abra "dados.json", adicione uma nova chave "cidade" com valor "São Paulo" e salve de volta.
8. Verifique se o arquivo "dados.json" existe antes de tentar carregá-lo e imprima uma mensagem apropriada.
9. Crie um arquivo JSON "numeros.json" com uma lista de números de 1 a 10.
10. Carregue "dados.json" e imprima cada item de uma lista como string separada por vírgula.
11. Substitua o valor da chave "idade" por 99 em "dados.json" e salve em um novo arquivo "modificado.json".
12. Carregue "dados.json" e imprima as chaves do dicionário raiz.
13. Conte quantas vezes o valor "São Paulo" aparece em valores de string no arquivo "dados.json".
14. Inverta a ordem de uma lista sob a chave "itens" em "dados.json" e salve em "invertido.json".
15. Carregue "dados.json", ordene alfabeticamente os valores de uma lista de strings e salve em "ordenado.json".
16. Encontre e imprima o valor numérico máximo em uma lista sob a chave "numeros" de "dados.json".
17. Remova chaves com valores nulos de "dados.json" e salve o resultado em "limpo.json".
18. Use o gerenciador de contexto (`with`) para carregar "dados.json" e imprimir seu tipo de dados raiz.
19. Crie um arquivo "nomes.json" extraindo apenas os valores de chaves "nome" de objetos em uma lista de "dados.json".
20. Carregue "dados.json" e imprima o tamanho total do arquivo em bytes.

#### Médio

21. Carregue dois arquivos JSON ("dados1.json" e "dados2.json") e mescle seus dicionários em um terceiro arquivo "uniao.json".
22. Procure por objetos em uma lista de "usuarios.json" onde o campo "idade" é maior que 30 e imprima esses objetos.
23. Trate um erro de JSON inválido ao tentar carregar "invalido.json" e imprima uma mensagem de erro personalizada.
24. Carregue "dados.json" com codificação UTF-8 e converta todas as strings para minúsculas, salvando em "minusculo.json".
25. Crie um dicionário de frequência de valores em um campo "categoria" de uma lista em "dados.json" e imprima as 5 mais comuns.
26. Adicione um campo "id" numerado (1, 2, 3...) a cada objeto em uma lista de "dados.json" e salve em "numerado.json".
27. Compare dois campos aninhados ("endereco.cidade") de "dados.json" e "referencia.json" e imprima diferenças em "diferencas.json".
28. Gere um backup de "dados.json" renomeando para "dados_backup.json" se o original existir.
29. Filtre "dados.json" removendo objetos onde "idade" < 18 e salve em "adultos.json".
30. Crie um arquivo "resumo.json" com estatísticas: contagem de objetos, média de "idade" e lista de categorias únicas de "dados.json".
31. Divida uma lista de objetos em "dados.json" em arquivos separados por valor do campo "categoria" (ex: tech.json, saude.json).
32. Encontre objetos em "dados.json" onde o campo "nome" é um palíndromo e liste-os.
33. Substitua valores em "dados.json" usando um dicionário de mapeamento (ex: {'SP': 'São Paulo'}) no campo "estado" e salve o resultado.
34. Carregue "dados.json" e "referencia.json", encontre objetos com "nome" comum e escreva em "comuns.json".
35. Trate exceções ao adicionar um campo novo em "dados.json" se o arquivo estiver corrompido (use try-except).
36. Processe todos os arquivos .json em um diretório e conte o total de objetos em listas de todos eles.
37. Adicione um campo "timestamp" com a data atual a cada objeto em uma lista de "dados.json" e salve.
38. Valide se "dados.json" tem uma estrutura específica (ex: raiz é lista com 5 objetos); se não, adicione objetos vazios até atingir e salve.
39. Extraia apenas valores numéricos de um campo "salario" em objetos de "dados.json" (usando regex simples) e salve em "salarios.json".
40. Calcule e adicione um campo "idade_media" (média global de idades) a cada objeto em "dados.json" e salve.

#### Difícil

41. Processe um JSON grande ("dados_grande.json") em chunks (usando ijson ou similar), contando totais por "categoria" sem carregar tudo na memória.
42. Use expressões regulares para validar e extrair e-mails de um campo "email" em objetos de "usuarios.json" e salve apenas objetos válidos em "validos.json".
43. Edite "dados.json" in-place removendo objetos duplicados baseados em múltiplos campos (sem criar cópia).
44. Parse "config.json" (formato chave=valor aninhado) em um dicionário e use-o para mapear campos em outro JSON "dados.json", salvando o mapeado.
45. Compare similaridade entre dois JSONs grandes ("versao1.json" e "versao2.json") calculando Jaccard em listas de valores e gere um relatório em "relatorio.json".
46. Gere um relatório consolidado de múltiplos JSONs de vendas ("vendas1.json" a "vendas5.json"), somando totais por "produto" e "regiao" em "consolidado.json".
47. Implemente uma substituição condicional em "dados.json": altere "salario" por valor médio apenas se "cargo" for "Gerente".
48. Leia "hierarquia.json" (com campos "funcionario" e "chefe"), construa um grafo de relações e salve uma versão de caminhos em "caminhos.json".
49. Otimize a busca em "dados_enorme.json" para filtrar por substring em um campo aninhado usando índices ou bibliotecas como ijson.
50. Integre manipulação de JSONs com validação: carregue "transacoes.json", processe em lista de dicionários, valide saldos cumulativos por "conta" e gere "auditoria.json" com discrepâncias.


## CSV

O **CSV** (*Comma Separated Values*), Valores Separados por Vírgula em tradução direta, é o formato mais comum para importação e exportação de dados para planilhas e bases de dados. Apesar de o nome indicar a separação de valores por vírugla, na realidade outros separadores podem ser utilizados. No [RFC 4180](https://datatracker.ietf.org/doc/html/rfc4180.html) é possível encontrar uma proposta de padronização do formato.

De modo geral um arquivo CSV vai conter a seguinte estrutura:

- **linha 1**: cabeçalho, com os nomes das colunas separados por vírgula.
- **demais linhas**: cada linha contém os valores de alguma observação separados por vírgula.

O módulo [csv](https://docs.python.org/3.13/library/csv.html), nativo do Python, implementa classes para leitura e escrita de dados tabulares no formato CSV. As duas principais funções do módulo são:

- [csv.reader(csvfile, /, dialect='excel', **fmtparams)](https://docs.python.org/3.13/library/csv.html#csv.reader)
  - Retorna um [*reader object*](https://docs.python.org/3.13/library/csv.html#reader-objects) que irá processar as linhas do arquivo CSV passado.
  - Se o *csvfile* é um objeto de arquivo, ele deve ser aberto com a opção `newline=''`.
  - O parâmetro `dialect` define um [conjunto de parâmetros para um dialeto](https://docs.python.org/3.13/library/csv.html#csv-fmt-params) particular de CSV. Por exemplo, é a partir dele que é possível definir como tratar aspas duplas, espaços em branco, delimitadores, etc.
  - Os parâmetros opcionais de `**fmtparams`, podem ser dados para sobrescrever parâmetros individuais do dialeto corrente.
- [csv.writer(csvfile, /, dialect='excel', **fmtparams)](https://docs.python.org/3.13/library/csv.html#csv.writer).

As principais classes implementadas pelo módulo são:

- [class csv.DictReader(f, fieldnames=None, restkey=None, restval=None, dialect='excel', *args, **kwds)](https://docs.python.org/3.13/library/csv.html#csv.DictReader)
  - Cria um objeto que opera como um *reader* regular, mas mapeia as informações de cada linha em um `dict`, cujas chaves são dadas pelo parâmetro opcional `fieldnames`.
  - Se o parâmetro `fieldnames` é omitido, os valores presentes na primeira linha do arquivo `f` serão usados como *fieldnames* e omitidos dos resultados. Porém, se o parâmetro é fornecido, os nomes serão usados, e os valores da primeira linha serão inclusos nos resultados.
  - Se uma linha tiver mais campos do que nomes de campos, os valores sobressalentes são armazenados no campo especificado por `restkey`.
  - Se uma linha não vazia tiver menos campos do que nomes de campos, os valores que faltam são preenchidos com o valor de `restval`.
- [class csv.DictWriter(f, fieldnames, restval='', extrasaction='raise', dialect='excel', *args, **kwds)](https://docs.python.org/3.13/library/csv.html#csv.DictWriter)
  - Cria um objeto que opera como um *writer* regular, mas mapeia dicionários às linhas da saída.
  - O parâmetro `fieldnames` é uma sequência que identifica a ordem no qual valores no dicionário passado para o método `writerow()` são escritos no arquivo `f`.

### Exemplos

- [Exemplo 1](exemplos/exemplo03.py)
- [Exemplo 2](exemplos/exemplo04.py)

### Exercícios

#### Fáceis

1. Crie um script que abra um arquivo CSV chamado "dados.csv" e imprima o cabeçalho (primeira linha).
2. Escreva um programa que crie um novo arquivo CSV chamado "saida.csv" com duas colunas: "Nome" e "Idade", e adicione uma linha de exemplo: "João, 25".
3. Leia "dados.csv" e imprima o valor da primeira coluna da primeira linha de dados (ignorando o cabeçalho).
4. Conte o número total de linhas (incluindo cabeçalho) em "dados.csv".
5. Leia "dados.csv" e imprima todos os valores da coluna "Nome" (assumindo que existe).
6. Copie o conteúdo inteiro de "entrada.csv" para um novo arquivo chamado "copia.csv".
7. Abra "dados.csv" e adicione uma nova linha no final: "Maria, 30, São Paulo".
8. Verifique se o arquivo "dados.csv" existe antes de tentar lê-lo e imprima uma mensagem apropriada.
9. Crie um arquivo CSV "numeros.csv" com uma coluna "Numero" contendo os números de 1 a 10.
10. Leia "dados.csv" e imprima cada linha como uma lista de strings.
11. Substitua o valor da coluna "Idade" na primeira linha de "dados.csv" por 99 e salve em um novo arquivo "modificado.csv".
12. Leia "dados.csv", divida em dicionários (usando cabeçalho como chaves) e imprima o primeiro dicionário.
13. Conte quantas linhas em "dados.csv" têm a palavra "São Paulo" na coluna "Cidade".
14. Inverta a ordem das linhas de dados (excluindo cabeçalho) de "dados.csv" e escreva em "invertido.csv".
15. Leia "dados.csv", ordene as linhas pela coluna "Nome" alfabeticamente e salve em "ordenado.csv".
16. Encontre e imprima a linha com o maior valor na coluna "Idade" de "dados.csv".
17. Remova linhas onde a coluna "Idade" está vazia em "dados.csv" e salve o resultado em "limpo.csv".
18. Use o gerenciador de contexto (`with`) para ler "dados.csv" e imprimir o número de colunas no cabeçalho.
19. Crie um arquivo "nomes.csv" extraindo apenas a coluna "Nome" de "dados.csv".
20. Leia "dados.csv" e imprima o tamanho total do arquivo em bytes.

#### Médios

21. Leia dois arquivos CSV ("dados1.csv" e "dados2.csv") e concatene-os em um terceiro arquivo "uniao.csv", preservando cabeçalhos.
22. Procure por linhas em "vendas.csv" onde a coluna "Produto" é "Notebook" e imprima essas linhas.
23. Trate um erro de arquivo CSV malformado ao tentar ler "invalido.csv" e imprima uma mensagem de erro personalizada.
24. Leia "dados.csv" com delimitador ';' (em vez de vírgula) e salve com delimitador padrão em "padrao.csv".
25. Crie um dicionário de frequência de valores na coluna "Cidade" de "dados.csv" e imprima as 5 cidades mais comuns.
26. Numere as linhas de dados em "dados.csv" adicionando uma coluna "ID" (1, 2, 3...) e salve em "numerado.csv".
27. Compare duas colunas de "dados.csv" ("Idade" e "Idade_Esperada") e imprima linhas onde diferem em "diferencas.csv".
28. Gere um backup de "dados.csv" renomeando para "dados_backup.csv" se o original existir.
29. Filtre "dados.csv" removendo linhas onde "Idade" < 18 e salve em "adultos.csv".
30. Crie um arquivo "resumo.csv" com estatísticas: contagem de linhas, média de "Idade" e lista de cidades únicas de "dados.csv".
31. Divida "dados.csv" em arquivos separados por valor da coluna "Cidade" (ex: sao_paulo.csv, rio.csv).
32. Encontre linhas em "dados.csv" onde o "Nome" é um palíndromo e liste-as.
33. Substitua valores em "dados.csv" usando um dicionário (ex: {'SP': 'São Paulo'}) na coluna "Cidade" e salve o resultado.
34. Leia "dados.csv" e "referencia.csv", encontre linhas com "Nome" comum e escreva em "comuns.csv".
35. Trate exceções ao adicionar uma coluna nova em "dados.csv" se o arquivo estiver corrompido (use try-except).
36. Processe todos os arquivos .csv em um diretório e conte o total de linhas em todos eles.
37. Adicione uma coluna "Data" com a data atual em todas as linhas de "dados.csv" e salve.
38. Valide se "dados.csv" tem exatamente 5 colunas; se não, adicione colunas vazias até atingir o número e salve.
39. Extraia apenas valores numéricos da coluna "Salario" em "dados.csv" (usando regex simples) e salve em "salarios.csv".
40. Calcule e adicione uma coluna "Idade_Media" (média global de idades) em cada linha de "dados.csv" e salve.

#### Difíceis

41. Processe um CSV grande ("vendas_grande.csv") em chunks de 1000 linhas, contando totais por "Produto" sem carregar tudo na memória (use pandas se preferir).
42. Use expressões regulares para validar e extrair CPFs da coluna "CPF" em "clientes.csv" e salve apenas linhas válidas em "validos.csv".
43. Edite "dados.csv" in-place removendo linhas duplicadas baseadas em todas as colunas (sem criar cópia).
44. Parse "config.csv" (formato chave=valor) em um dicionário e use-o para mapear colunas em outro CSV "dados.csv", salvando o mapeado.
45. Compare similaridade entre dois CSVs grandes ("versao1.csv" e "versao2.csv") calculando Jaccard por linhas e gere um relatório em "relatorio.csv".
46. Gere um relatório consolidado de múltiplos CSVs de vendas ("vendas1.csv" a "vendas5.csv"), somando totais por "Produto" e "Regiao" em "consolidado.csv".
47. Implemente uma substituição condicional em "dados.csv": altere "Salario" por valor médio apenas se "Cargo" for "Gerente".
48. Leia "hierarquia.csv" (com colunas "Funcionario", "Chefe"), construa um grafo de relações e salve uma versão de caminhos em "caminhos.csv".
49. Otimize a busca em "dados_enorme.csv" para filtrar por substring na coluna "Descricao" usando índices de pandas ou similar.
50. Integre manipulação de CSVs com validação: leia "transacoes.csv", processe em DataFrame, valide saldos cumulativos por "Conta" e gere "auditoria.csv" com discrepâncias.