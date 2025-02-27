num = int(input("Digite um número: "))
novo_num = str(num)
inverso = novo_num[::-1]
novo_inverso = int(inverso)
print(novo_inverso)

if num == novo_inverso: 
    print("O número digitado é um Palíndromo")