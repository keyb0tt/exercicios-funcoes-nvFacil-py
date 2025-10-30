# Crie uma função contar_vogais(texto) que conte e retorne o número de vogais em uma string.
import os
os.system('clear')

def contar_vogais(texto):
    cont_vogais = 0
    vogais = 'aeiou'
    lista_letras = list(texto)

    for letra in lista_letras:
        if letra.lower() in vogais:
            cont_vogais += 1

    return cont_vogais

qnt_vogais = contar_vogais('Exemplo')
print(f'{qnt_vogais=}')