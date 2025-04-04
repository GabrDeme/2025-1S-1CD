# fila 

from collections import deque
fila  = deque()

# enfileirar 
fila.append(10)
fila.append(8)
fila.append(55)

print(fila)

# primeiro da fila
print("Primeiro da fila:", fila[0])

# desenfileirando o primeiro da fila
print("Removido:", fila.popleft(), "Primeiro da fila:", fila[0])

print("Fila está vazia? ", "Sim" if len(fila) == 0 else "Não")