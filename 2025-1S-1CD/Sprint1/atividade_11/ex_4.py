maior_num = int(input("Insira um número: "))

while True:
    num = int(input("Digite um número (digite 0 para parar): "))

    if num == 0:
        break

    if num > maior_num:
        maior_num = num

print(maior_num)