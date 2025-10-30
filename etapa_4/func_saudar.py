# Crie uma função saudar(nome="Visitante") que mostre uma mensagem de boas-vindas,
# usando o nome fornecido (ou “Visitante” por padrão).
import os
os.system('clear')

def saudar(nome='Visitante'):
    print(f'Boas-vindas, {nome}!')

saudar()
saudar('Toninho')