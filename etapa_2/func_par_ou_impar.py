# Crie uma função par_ou_impar(num) que informe se um número é par ou ímpar.
import os
os.system('clear')

def par_ou_impar(num):
    if num % 2 == 0:
        return True
    else:
        return False
    
numero = int(input('Informe o número desejado: '))

cond_numero = par_ou_impar(numero)

if cond_numero == True:
    print('O Número inserido é par.')
else:
    print('O Número inserido é ímpar.')