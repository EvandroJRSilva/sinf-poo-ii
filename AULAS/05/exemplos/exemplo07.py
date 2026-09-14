import os

with open("./AULAS/05/exemplos/teste3.txt", "w") as arquivo:
    arquivo.write("Cubo Mágico")

if os.path.exists("teste3.txt"):
    os.remove("teste3.txt")
else:
    print("Arquivo não existe")