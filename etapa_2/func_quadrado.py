# Crie uma função quadrado(n) que receba um número e mostre seu quadrado.
import os
os.system('clear')

def quadrado(n):
    resultado = n * n 
    return resultado

n = 10

resultado_quadrado = quadrado(n)
print(f'{resultado_quadrado=}')