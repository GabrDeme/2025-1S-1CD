# FOR

# num = int(input("Informe um número: "))
# info = len(str(abs(num)))
# contador = 0

# for n in range(info):
#     contador += 1
# print(f"O número {num} tem {contador} dígitos")

# WHILE

num = int(input("Informe um número: "))
contador = 0

while num > 0:
    num //= 10
    contador += 1
print(f"O número {num} tem {contador} dígitos")