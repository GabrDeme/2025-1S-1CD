candidato1 = 0
candidato2 = 0
candidato3 = 0
candidato4 = 0
nulo = 0
branco = 0

qnt = 0

num = int(input("Quantas pessoas serão listadas? \n"))

while True:
    qnt += 1
    if num < qnt:
        break
    voto = int(input("""Escolha um dos seguintes números de voto para os candidatos: 
          1 -> Candidato 1
          2 -> Candidato 2
          3 -> Candidato 3
          4 -> Candidato 4
          5 -> Nulo
          6 -> Branco
          """))
    match voto:
        case 1:
            candidato1 += 1
        case 2:
            candidato2 += 1
        case 3:
            candidato3 += 1
        case 4:
            candidato4 += 1
        case 5:
            nulo += 1
        case 6:
            branco += 1
        case _:
            print("Você votou em um valor não válido!")
print(f"""
O resultado da eleição foi:
Candidato 1 = {candidato1} votos
Candidato 2 = {candidato2} votos
Candidato 3 = {candidato3} votos
Candidato 4 = {candidato4} votos
Nulo = {nulo} votos
Branco = {branco} votos
""")