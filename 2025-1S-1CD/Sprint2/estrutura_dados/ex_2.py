# Crie uma função que receba uma lista de tuplas, onde cada tupla 
# contém o nome de um aluno e sua nota, e retorne o nome do aluno 
# com a maior nota.

alunos = [("João", 8.5), ("Maria", 9.2), ("Pedro", 7.8)]

def maior_nota(lista_de_alunos):
    aluno = max(lista_de_alunos, key=lambda x: x[1])
    return aluno[0]

print(maior_nota(alunos))