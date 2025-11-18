import requests

# Fazendo uma requisição GET simples
r = requests.get('https://ufpi.br')
print(r.status_code)
print(r.headers['Server'])

# Verificando se a página contém o nome da universidade
if 'Universidade Federal do Piauí' in r.text:
    print('O nome da universidade está na página')
else:
    print('A página não tem o nome da universidade')
    
# Baixando o logo ddo site
logo_url = 'https://ufpi.br/templates/templatedefault/favicon.ico'
r = requests.get(logo_url)

with open('AULAS/08/exemplos/logo_ufpi.ico', 'wb') as f:
    f.write(r.content)
    
print(f'Logo baixado com sucesso! Tamanho: {len(r.content)} bytes')