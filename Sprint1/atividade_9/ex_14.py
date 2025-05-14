for i in range(10000):
    num = int(input("Informe um nota entre 0 e 10: "))
    if num > 10:
        print("😒 Número inválido!")
    else:
        print("😊 Número válido!")
        break