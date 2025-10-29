# Crie uma função soma(a, b) que receba dois números e mostre a soma deles.
import os
os.system('clear')

def soma(a, b):
    soma = a + b
    return soma

a = 10
b = 5

soma_numeros = soma(a, b)
print(f'{soma_numeros=}')