# Crie uma função media(a, b, c) que calcule e retorne a média de três números.
import numpy as np
import os
os.system('clear')

def media(a, b, c):
    numeros = [a, b, c]
    media = np.sum(numeros) / len(numeros) 

    return media


a = 10
b = 10
c = 13

media_num = media(a, b, c)
print(media_num)