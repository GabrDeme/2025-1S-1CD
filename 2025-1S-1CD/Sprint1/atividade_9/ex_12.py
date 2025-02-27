candidato1 = 0
candidato2 = 0
candidato3 = 0

num = int(input("Quantas pessoas serão listadas? \n"))

for n in range(num):
    voto = int(input("""Escolha um dos seguintes números de voto para os candidatos: 
          1 -> Candidato 1
          2 -> Candidato 2
          3 -> Candidato 3
          """))
    if voto == 1:
        candidato1 += 1
    elif voto == 2:
        candidato2 += 1
    elif voto == 3:
        candidato3 += 1
    else:
        print("Você votou em um valor não válido, agora você votou nulo")
print(f"""
O resultado da eleição foi:
Candidato 1 = {candidato1} votos
Candidato 2 = {candidato2} votos
Candidato 3 = {candidato3} votos
""")