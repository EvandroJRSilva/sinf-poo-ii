import csv

with open("./AULAS/06/exemplos/housing.csv", newline='') as meu_csv:
    leitor = csv.DictReader(meu_csv)
    fields = leitor.fieldnames
    print(f'Nomes das colunas: {', '.join(fields)}')
    
    linhas = list(leitor) # <--- aqui
    print(f'Quantidade de linhas: {len(linhas)}')

# Passando fieldnames -> primeira linha aparece nos resultados    
# with open("./AULAS/06/exemplos/housing.csv", newline='') as meu_csv:
#     leitor = csv.DictReader(meu_csv, fieldnames=['longitude','latitude','housing_median_age',
#                                                      'total_rooms','total_bedrooms','population',
#                                                      'households','median_income','median_house_value',
#                                                      'ocean_proximity'])
    
#     fields = leitor.fieldnames
#     print(f'Nomes das colunas: {', '.join(fields)}')
    
#     linhas = list(leitor)
#     print(f'Quantidade de linhas: {len(linhas)}')