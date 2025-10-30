# Crie uma função eh_primo(n) que retorne True se o número for primo, e False caso contrário.
import numpy as np
import os
os.system('clear')

def eh_primo(n):
    qnt_div = 0

    for i in range(n):
        if n % (i + 1) == 0:
            qnt_div += 1

    if qnt_div == 2 or n == 1:
        return True
    
    return False

cond_primo = eh_primo(int(input('Insira o número desejado: ')))

if cond_primo == True:
    print('É primo')
else:
    print('Não é primo')
