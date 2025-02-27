numeros = []

for dois in range(2):
    pergunta = int(input(f"Informe o {dois + 1}º número: "))
    numeros.append(pergunta)

for p in range(numeros[0], numeros[1] + 1):
    print(p)