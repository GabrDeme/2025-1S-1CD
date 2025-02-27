soma = 0
num = int(input("Quantas pessoas serão listadas? \n"))
for p in range(num):
    idade = int(input(f"Idade da pessoa {p+1}: "))
    soma += idade
resultado = soma / num
print(f"A média das idades dos alunos da turma é {resultado:.2f}")

if resultado < 25:
    print("Turma jovem")
elif resultado < 60:
    print("Turma adulta")
else:
    print("Turma idosa")