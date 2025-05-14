# Crie uma função que receba duas listas de números inteiros e 
# retorne uma nova lista contendo os elementos que aparecem em ambas 
# as listas (interseção).
lista_a = []
lista_b = []
lista = []

def lista_num(lista_a, lista_b, lista):
    while True:
        a = input("Digite os números que devem ser adicionados à lista A (dê ENTER caso queira encerrar): ")
        if a == "":
            break
        try:
            lista_a.append(int(a))
        except ValueError:
            print("Por favor, digite um número válido.")

    while True:
        b = input("Digite os números que devem ser adicionados à lista B (dê ENTER caso queira encerrar): ")
        if b == "":
            break
        try:
            lista_b.append(int(b))
        except ValueError:
            print("Por favor, digite um número válido.")

    for i in lista_a:
        if i in lista_b:
            lista.append(i)

    return lista
    

print(lista_num(lista_a, lista_b, lista))