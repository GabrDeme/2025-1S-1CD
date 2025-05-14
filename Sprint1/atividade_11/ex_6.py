nota = int(input("Insira uma nota entre 1 e 10: "))

while True:
    if nota < 0 or nota > 10:
        print("Informe um novo número")
        nota = int(input("Insira uma nota entre 1 e 10: "))
    else:
        print("Nota contabilizada")
        break