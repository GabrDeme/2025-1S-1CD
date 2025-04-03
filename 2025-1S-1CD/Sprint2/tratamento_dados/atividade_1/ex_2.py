# Crie uma pilha utilizando uma lista.

pilha = []

# Empilhe 3 números inteiros de sua escolha.

pilha.append(87)
pilha.append(23)
pilha.append(27)

# Mostre o topo da pilha.
print("Topo da pilha:", pilha[-1])

# Desempilhe o topo e mostre o novo topo.
print("Removido:", pilha.pop(), "Último número da lista:", pilha[-1])

# Tente desempilhar todos os elementos e mostrar se a pilha ficou vazia.
valores = len(pilha)

for i in range(valores):
    valor = pilha[-1]
    print("Removido:", pilha.pop())
    print("Pilha está vazia? ", "Sim" if len(pilha) == 0 else "Não")
