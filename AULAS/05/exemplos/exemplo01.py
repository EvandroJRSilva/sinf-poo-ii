arquivo = open("./AULAS/05/exemplos/teste.txt", "r")

print(arquivo.readable())  # imprimindo a verificação se o arquivo pode ser lido
print(arquivo.read())      # imprimindo o arquivo

arquivo.close()