"""
    Faça um programa que simule o lançamento de um dado. 
    O usuário deve escolher quantos dados jogar e o programa deve exibir os resultados.
"""

import random

def obter_lado_aleatorio_dado() -> int:
    """ Gera um lado aleatório de um dado lançado """
    return random.randint(1, 6)

def obter_quantidade_dados() -> int:
    """ Obtem a quantidade válida de dados a serem lançados pelo usuário """
    while True:
        try:
            qtd_dados = int(input("Informe a quantidade de dados: "))
            
            if qtd_dados <= 0: 
                Exception()
                
            return qtd_dados
        except: 
            print("Número inválido")
            
dados = obter_quantidade_dados()

for dado in range(dados):
    lado_dado = obter_lado_aleatorio_dado()
    print(f"Lado dado {dado + 1}: {lado_dado}")

