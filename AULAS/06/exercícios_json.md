# Exercícios JSON

## Questões Fáceis (1-20)
Essas questões focam em operações básicas de carregamento, salvamento e acesso a dados simples em arquivos JSON usando o módulo `json`.

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

## Questões de Dificuldade Média (21-40)
Essas questões envolvem manipulação de estruturas aninhadas, filtragem, tratamento de erros e operações com múltiplos JSONs.

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

## Questões de Dificuldade Alta (41-50)
Essas questões demandam complexidade maior, como manipulação eficiente de JSONs grandes, validação avançada, junções e integração com estruturas de dados complexas.

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