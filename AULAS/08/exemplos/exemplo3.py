import requests

# Seguindo redirecionamentos e ver o histórico
r = requests.get('http://ufpi.br', allow_redirects=True)
print(f'URL final após redirecionamentos: {r.url}')
print('Histórico de redirecionamentos:')
for h in r.history:
    print(f' → {r.status_code} {r.url}')