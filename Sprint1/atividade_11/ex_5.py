vezes = 0
igual_num = int(input("Insira um número: "))

while True:
    vezes += 1

    num = int(input("Digite um número (digite um número igual para parar o programa): "))
    if num == igual_num:
        break
    igual_num = num

print(f"Você digitou {igual_num} duas vezes iguais. E digitou {vezes} números")