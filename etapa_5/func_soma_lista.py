# Crie uma função soma_lista(lista) que receba uma lista de números e retorne a soma total.
import os
os.system('clear')

def somar_lista(lista):
    soma = sum(lista)

    return soma

numeros = [1, 2, 3, 4, 5]
soma_lista = somar_lista(numeros)

print(f'{soma_lista}')