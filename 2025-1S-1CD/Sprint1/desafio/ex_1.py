num = int(input("Insira um número: "))
num_inicial, mais_num = 0, 1

if num >= 0:
    print(num_inicial, end=" ")

while mais_num <= num:
    print(mais_num, end=" ")
    mais_num, num_inicial = num_inicial + mais_num, mais_num 