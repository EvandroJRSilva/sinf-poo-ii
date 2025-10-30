import csv
import json

qualquer = {'longitude': 1412421, 'latitude': 94823095823}

# with open("./AULAS/06/teste_json.json", "w") as meu_json:
#    json.dump(qualquer, meu_json, indent=4)
    
with open("./AULAS/06/exemplo.json", "r") as meu_json:
    trabalhos = json.load(meu_json)

    for trabalho in trabalhos:
        print(trabalho['nome'])
        for membro in trabalho['membros']:
            print(f'\t{membro["nome"]} é especialista em {membro['especialidade']}.')