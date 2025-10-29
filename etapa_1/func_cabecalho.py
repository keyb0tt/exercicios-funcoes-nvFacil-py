# Crie uma função cabecalho() que mostre um título formatado, com linhas acima e abaixo.
import os
os.system('clear')

def linha():
    print('-' * 30)

def cabecalho():
    linha()
    print('Esse é o título do cabeçalho')
    linha()

cabecalho()