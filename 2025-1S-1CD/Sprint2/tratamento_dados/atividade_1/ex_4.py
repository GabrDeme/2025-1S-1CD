# Crie uma fila vazia.

from collections import deque
fila  = deque()

# Enfileire 3 números inteiros na fila.
fila.append(13)
fila.append(67)
fila.append(21)

# Mostre o primeiro elemento da fila.
print("Primeiro da fila:", fila[0])

# Desenfileire o primeiro elemento e mostre o novo primeiro elemento.
print("Removido:", fila.popleft(), "Primeiro da fila:", fila[0])

#Verifique se a fila está vazia após as remoções.
print("Fila está vazia? ", "Sim" if len(fila) == 0 else "Não")