import csv

with open('./AULAS/06/exemplos/nomes.csv', 'w', newline='') as meu_csv:
    fieldnames = ['nome', 'sobrenome']
    writer = csv.DictWriter(meu_csv, fieldnames=fieldnames)
    
    writer.writeheader()
    writer.writerow({'nome': 'Fulano', 'sobrenome': 'da Silva'})
    writer.writerow({'nome': 'Cicrano', 'sobrenome': 'Pereira'})
    writer.writerow({'nome': 'Deltano', 'sobrenome': 'Ferreira'})