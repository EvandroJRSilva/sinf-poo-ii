import json

dados = {
    "nome": "Júlia",
    "idade": 30,
    "habilidades": ["Python", "POO II"],
    "ativo": True
}

# Criando uma string JSON formatada
json_string = json.dumps(dados, indent=4)
print(json_string)

# Salvando diretamente em um arquivo
with open(".AULAS/06/exemplos/usuario.json", "w") as arquivo:
    json.dump(dados, arquivo, indent=4, ensure_ascii=False)