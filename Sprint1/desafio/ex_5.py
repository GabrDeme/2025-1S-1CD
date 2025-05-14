import math

num = int(input("Informe um número: "))
raiz = math.sqrt(num)
print(raiz)
if raiz == 0:
    print(f"{num} é um quadrado perfeito")
else:
    print(f"{num} não é um quadrado perfeito")