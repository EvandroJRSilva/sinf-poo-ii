import json, os

# Uma string JSON (geralmente recebida de uma API)
json_input = '{"nome": "João", "empresa": null, "estudante": true,"disciplinas": [{"nome": "POO 2","período": 4},{"nome": "PWeb 1","período": 4}]}'

# Convertendo para dicionário Python
objeto_python = json.loads(json_input)

print(objeto_python["nome"])  # Saída: João
print(objeto_python["disciplinas"][0]["nome"]) # Saída: POO 2
print(type(objeto_python))     # Saída: <class 'dict'>

objeto_python["disciplinas"].append({"nome": "Redes 1", "período":4})
print(objeto_python["disciplinas"]) # Saída: dicionário atualizado


# Lendo de um arquivo
with open("./AULAS/06/exemplos/usuario.json", 'r+') as arquivo:
    dados_carregados = json.load(arquivo)
    
    for usuario in dados_carregados:
        print(f"Nome: {usuario['nome']}\nIdade: {usuario['idade']}\nHabilidades:{usuario['habilidades']}")
    
    dados_carregados.append({"nome":"Deltano", "idade":30,"habilidades":["Java", "C++"],"ativo":False})
    print(dados_carregados[2])
    
    # Sobrescrevendo. É possível por causa do r+
    # Configurando o cursor (stream position) para o início do arquivo, para sobrescrever
    arquivo.seek(0, os.SEEK_SET)
    json.dump(dados_carregados, arquivo, ensure_ascii=False, indent=4)