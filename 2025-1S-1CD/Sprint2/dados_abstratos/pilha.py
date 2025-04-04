# pilha

pilha = []

# empilhando

pilha.append(10)
pilha.append(8)
pilha.append(55)

print(pilha)

# topo da pilha
print("Topo da pilha:", pilha[-1])

# desempilhando
print("Removido:", pilha.pop(), "Lista atual:", pilha)

print("Pilha está vazia? ", "Sim" if len(pilha) == 0 else "Não")