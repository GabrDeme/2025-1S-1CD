# Crie um programa que simule um dicionário de contatos.
# O programa deve permitir adicionar novos contatos 
# (nome e número de telefone), buscar o número de telefone de um 
# contato pelo nome e listar todos os contatos.

contatos = {
    "Mario" : 40028922
}

print("Bem-vindo a sua lista de contatos")
while True:
    n = input("""O que você deseja fazer?
              1 - Adicionar um novo contato
              2 - Deletar um contato
              3 - Procurar número por nome
              4 - Listar todos os contatos  

              Caso deseje sair pressione ENTER   

              """)
    if n == "":
        break

    try:
        N = int(n)
    except ValueError:
        print("Por favor, digite um número válido. ")
    
    match N:
        case 1:
            nome = input("Qual seria o nome do contato? ")
            numero = input("Qual seria o número do contato? ")

            contatos[nome] = numero

            print(contatos)
        case 2:
            nome = input("Qual seria o nome do contato? ")

            if nome in contatos:
                del contatos[nome]

                print(contatos)
            else:
                print("Esse nome não existe dentro de contatos.")
        case 3:
            nome = input("Qual seria o nome do contato? ")

            if nome in contatos:
                print(contatos[nome])

                print(contatos)
            else:
                print("Esse nome não existe dentro de contatos.")
        case 4:
            print("Aqui está a sua lista de contatos: ")
            print(contatos)
        case _:
            print("""Esse não é um valor válido!
                  Tente Novamente ou pressione ENTER para sair

                  """)