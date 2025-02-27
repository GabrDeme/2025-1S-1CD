geral = 0
for f in range(5):
    faturamento = float(input(f"Digite o faturamento do {f+1}º cliente: "))

    geral += faturamento

if geral >= 54000:
    print(f"O faturamento foi superior que o da Americanas em R$ {geral - 54000:.2f}")
else:
    print(f"Perdeu pra Americanas em R$ {34000 - geral:.2f} kkkkkkkkk")
