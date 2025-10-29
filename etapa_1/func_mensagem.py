# Crie uma função mensagem() que exiba seu nome e curso na tela.
import os
os.system('clear')

def mensagem(nome, curso):
    print(f'Meu nome é {nome}, eu estou cursando {curso}')

nome = 'Kaique'
curso = 'Engenharia de Software'

mensagem(nome, curso)