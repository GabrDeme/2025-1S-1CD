produtos = {
    1: {'nome': 'Produto A', 'preco': 10.00},
    2: {'nome': 'Produto B', 'preco': 20.00},
    3: {'nome': 'Produto C', 'preco': 15.00},
    4: {'nome': 'Produto D', 'preco': 25.00}
}

total = 0

while True:
    p = int(input("Digite o código do item: "))
    if p == 0:
        print("Obrigado pela compra!")
        break
    if p not in produtos:
        print("Código inválido! Tente novamente.")
        continue

    q = int(input(f"Informe a quantidade que você deseja do produto {produtos[p]['nome']}: "))
    if q <= 0:
        print("Quantidade inválida. Tente novamente.")
        continue

    preco = produtos[p]['preco']
    total += preco * q 

print(f"O total da sua compra é R$ {total:.2f}")
