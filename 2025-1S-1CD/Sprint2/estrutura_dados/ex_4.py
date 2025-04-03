# Crie uma função que receba duas listas de números inteiros e 
# retorne um conjunto com os números que aparecem em ambas as listas.

def intersecao_listas(lista1, lista2):
    return set(lista1) & set(lista2)

lista1 = [1, 2, 3, 4, 5]
lista2 = [3, 4, 5, 6, 7]
resultado = intersecao_listas(lista1, lista2)
print(resultado)