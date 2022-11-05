"""
Pilhas e filas
Pilha (Stack) - LIFO - last in, first out.
    Exemplo: Pilha de livros que são adicionaos um sobre o outro.
Fila (queue) - FIFO - first in, first out.
    Exemplo: Uma fila de banco (ou qualquer fila da vida real)
Filas podem ter efeitos colaterais em desempenho, porque a cada item
alterado, todos os índices serão modificados.
"""
from collections import deque
from time import sleep

fila = deque(maxlen=10)
fila.extend([1,2,3,4,5,6, 7, 8, 9, 10])
fila.rotate(1)
print(fila)

# for i in range(1000):
#     fila.append(i)
#     print(fila)


# fila.append('João')
# fila.append('Mathias')
# fila.append('Miranda')
# fila.append('Vinicius')
# fila.append('Allan')
# print(f'Leave: {fila.popleft()}')
# print(f'Leave: {fila.popleft()}')
# print(f'Leave: {fila.popleft()}')
# print(f'Leave: {fila.popleft()}')
# for name in fila:
#     print(name)
