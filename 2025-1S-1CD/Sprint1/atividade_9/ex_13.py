impares = 0
pares = 0

for n in range(10):
    num = int(input(f"Número {n+1}: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
print(f"""
Quantidade:
Pares = {pares}
Impares = {impares}
      """)