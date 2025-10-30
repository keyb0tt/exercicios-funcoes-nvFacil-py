# Crie uma função potencia(base, expoente=2) que calcule a potência de um número (padrão é ao quadrado).
import os
os.system('clear')

def potencia(base, expoente=2):
    soma = base
    for i in range(expoente - 1):
        soma *= base

    return soma

print(f'{potencia(5)=}')
print(f'{potencia(5, 3)=}')
