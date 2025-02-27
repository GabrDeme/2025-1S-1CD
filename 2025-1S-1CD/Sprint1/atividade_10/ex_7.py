num = int(input("Escolha um número secreto entre 1 e 10: "))

while num != 7:
    print("Esse não é o número secreto!")
    num = int(input("Escolha um número secreto entre 1 e 10 novamente: "))
print("\nParabéns você descobriu que o número secreto é 7")