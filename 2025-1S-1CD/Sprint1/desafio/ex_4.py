
num = int(input("Digite um número inteiro positivo: "))

soma = 0
i = 1

while i < num:
    if num % i == 0:
        soma += i
    i += 1

if soma == num:
    print(f"{num} é um número perfeito")
else:
    print(f"{num} não é um número perfeito")
