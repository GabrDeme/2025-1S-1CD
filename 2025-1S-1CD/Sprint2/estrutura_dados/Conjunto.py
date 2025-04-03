frutas = ["maça","banana","uva"]
print(frutas)

frutas.append("morango")
print(frutas)

frutas.remove("banana")
print(frutas)

frutas.append("morango")
print(frutas)

print("maça" in  frutas)

print("abacate" in  frutas)

# Operações entre conjuntos

conjunto_a = {1,2,3,4}
conjunto_b = {4,0,2,9}

uniao = conjunto_a | conjunto_b
print(uniao)

interseccao = conjunto_a & conjunto_b
print(interseccao)

diferenca = conjunto_a - conjunto_b
print(diferenca)

diferenca_simetrica = conjunto_a ^ conjunto_b
print(diferenca_simetrica)