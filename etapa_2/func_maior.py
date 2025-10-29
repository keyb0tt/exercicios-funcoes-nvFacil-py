# Crie uma função maior(a, b) que receba dois números e mostre qual é o maior.
import os
os.system('clear')

def maior(a, b):
    numeros = [a, b]
    maior = max(numeros)

    return maior

a = 30
b = 20
maior_num = maior(a, b)

print(f'{maior_num=}')
