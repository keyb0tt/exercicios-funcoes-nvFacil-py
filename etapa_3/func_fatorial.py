# Crie uma função fatorial(n) que calcule e retorne o fatorial de um número.
import numpy as np
import os
os.system('clear')

def fatorial(n):
    resultado_fatorial = np.math.factorial(n)

    return resultado_fatorial

numero = int(input('Insira o número desejado: '))
os.system('clear')

fatorial_numero = fatorial(numero)

print(f'O Fatorial de {numero} é igual a {fatorial_numero}')
