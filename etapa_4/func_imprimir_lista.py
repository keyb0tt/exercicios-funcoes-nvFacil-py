# Crie uma função imprimir_lista(lista, titulo="Minha Lista") que mostre um título e depois 
# todos os elementos da lista.
import os
os.system('clear')

def imprimir_lista(lista, titulo="Minha Lista"):
    print(f'--------------------{titulo}--------------------\n')
    print(f'{lista}\n')
    print(f'---------------------------------------------------\n')

lista = ['Arroz', 'Fejao', 'Batata', 'Betoneira']

imprimir_lista(lista)