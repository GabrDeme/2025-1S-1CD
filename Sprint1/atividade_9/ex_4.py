numeros = []

for n in range(5):
    num = int(input(f"Informe o {n+1} número a ser adicionado à lista: "))
    numeros.append(num)
    print(numeros)

soma = sum(numeros)
print(f"\nO resultado da soma de todos os números é {soma}")
print(f"E sua média é {soma/5:.2f}")
