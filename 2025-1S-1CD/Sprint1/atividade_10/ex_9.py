num = int(input("Digite um número: "))
qnt = 0

while True:
    if num % 2 == 0:
        qnt += 1
    num = int(input("Digite um número: "))

    if num < 0:
        print("Programa finalizado")
        print(f"""\nVocê digitou um número menor que 0!
E você digitou {qnt} números pares""")
    