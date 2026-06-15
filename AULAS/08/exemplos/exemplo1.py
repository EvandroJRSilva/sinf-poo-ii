import requests

# Fazendo uma requisição GET simples
r = requests.get('https://ufpi.br')
print(r.status_code)
print(f'Tamanho da página: {len(r.text)} caracteres')
#print(r.headers['Server'])
print(r.headers)

# Verificando se a página contém o nome da universidade
if 'Universidade Federal do Piauí' in r.text:
    print('O nome da universidade está na página')
else:
    print('A página não tem o nome da universidade')
    
# Baixando o logo do site
logo_url = 'https://ufpi.br/images/assets/ufpi-icone1%201.png#joomlaImage://local-images/assets/ufpi-icone1%201.png?width=99&height=149'
r = requests.get(logo_url)

if r.status_code == 200:
    print(f'Logo baixado com sucesso! Tamanho: {len(r.content)} bytes')

with open('AULAS/08/exemplos/logo_ufpi.ico', 'wb') as f:
    #print(r.content)
    f.write(r.content)