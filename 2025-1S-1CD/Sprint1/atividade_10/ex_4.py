senha = int(input("Digite a sua senha: "))

while senha != 1234:
    print("Senha incorreta!")
    senha = int(input("Digite a sua senha novamente: "))

print("Senha correta!")