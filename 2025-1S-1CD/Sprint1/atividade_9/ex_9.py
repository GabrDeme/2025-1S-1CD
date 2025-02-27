primo = int(input("Digite um número: "))
if num < 2:
    print("Não é primo")
else:
    for p in range(2, primo+1):
        if num % i == 0:
            print("Não é primo")
            break
        else: 
            print("É Primo")