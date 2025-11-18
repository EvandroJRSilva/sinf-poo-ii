import requests

# Simulando o acesso ao site a partir de algum navegador
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

r = requests.get('https://ufpi.br', headers=headers)
print(f'Status: {r.status_code}')
print(f'Tamanho da página: {len(r.text)} caracteres')