import json

# Uma string JSON (geralmente recebida de uma API)
json_input = '{"nome": "João", "empresa": null, "estudante": false}'

# Convertendo para dicionário Python
objeto_python = json.loads(json_input)

print(objeto_python["nome"])  # Saída: João
print(type(objeto_python))     # Saída: <class 'dict'>

# Lendo de um arquivo
with open("./AULAS/06/exemplos/usuario.json") as arquivo:
    dados_carregados = json.load(arquivo)
    print(dados_carregados)