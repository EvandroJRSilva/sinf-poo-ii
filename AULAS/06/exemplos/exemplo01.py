import json

dados = {
    "nome": "Fulano",
    "idade": 20,
    "habilidades": ["Python", "Java"],
    "ativo": True
}

# Criando uma string JSON formatada
json_string = json.dumps(dados, indent=2, ensure_ascii=False)
print(json_string)

# Salvando diretamente em um arquivo
with open(".AULAS/06/exemplos/usuario.json", "w") as arquivo:
    json.dump(dados, arquivo, indent=4, ensure_ascii=False)