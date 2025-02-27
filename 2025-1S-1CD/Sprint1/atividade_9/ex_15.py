reais = 400
desconto = 0

print("Valor - % de desconto - Valor Final")
for d in range(100):
    reais += 100
    desconto += 1
    print(f"R$ {reais} - {desconto}% - R$ {reais*(0.01 * desconto):.2f}")