# Crie uma função area_retangulo(base, altura) que retorne a área do retângulo.
import os
os.system('clear')

def area_retangulo(base, altura):
    area = base * altura

    return area

base = int(input('Insira a base do retângulo em cm: '))
os.system('clear')

altura = int(input('Insira a altura do retângulo em cm: '))
os.system('clear')

area = area_retangulo(base, altura)

print(f'A área do retângulo é de {area} cm')