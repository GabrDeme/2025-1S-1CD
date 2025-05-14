while True:
    total = 0
    print("Bem-vindo à caixa registradora!")
    
    while True:
        valor_produto = float(input("Digite o valor do produto (ou 0 para encerrar a compra): "))
        
        if valor_produto == 0:
            break 
            
        total += valor_produto 
        
    print(f"\nTotal da compra: R${total:.2f}")
    
    while True:
        valor_pago = float(input("Digite o valor pago pelo cliente: R$"))
        
        if valor_pago < total:
            print("O valor pago é insuficiente. Por favor, insira um valor maior ou igual ao total.")
        else:
            break
    
    troco = valor_pago - total
    print(f"Troco a ser devolvido: R${troco:.2f}")
    
    resposta = input("\nDeseja registrar outra compra? (s/n): ").lower()
    if resposta != 's':
        print("Obrigado pela compra! Até logo!")
        break
