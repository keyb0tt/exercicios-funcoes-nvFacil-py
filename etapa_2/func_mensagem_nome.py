# Crie uma função mensagem_nome(nome) que receba um nome e mostre uma saudação personalizada.
import os
os.system('clear')

def mensagem_nome(nome):
    print(f'Olá {nome}!\nSeja bem-vindo!')

nome = 'Kaique'

mensagem_nome(nome)