# Crie uma pilha vazia (utilizando uma lista).

pilha = []

# Empilhe (adicione) os números 5, 10 e 15 na pilha.

pilha.append(5)
pilha.append(10)
pilha.append(15)

# Mostre o topo da pilha (último elemento).
print("Topo da pilha:", pilha[-1])

# Desempilhe (remova) o topo da pilha e mostre o novo topo.
print("Removido:", pilha.pop(), "Último número da lista:", pilha[-1])

# Verifique se a pilha está vazia e imprima o resultado.
print("Pilha está vazia? ", "Sim" if len(pilha) == 0 else "Não")