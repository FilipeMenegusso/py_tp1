"""
    Crie um programa que apresente ao usuário uma série de escolhas (como em uma história) 
        e conduza a diferentes resultados com base nessas escolhas.
"""

from enum import Enum
from typing import List


class TipoEscolha(Enum):
    PROGRAMADOR = 1
    FRONT = 2
    BACK = 3
    ESTUDA_TI = 4
    
criacao_historia = [
    [TipoEscolha.PROGRAMADOR, "Você é programador(a)?", "Programador(a)"],
    [TipoEscolha.ESTUDA_TI, "Você estuda TI?", "Estudante de TI"],
    [TipoEscolha.FRONT, "Você quer ser Front-End?", "Front-End"],
    [TipoEscolha.BACK, "Você quer ser Back-End?", "Back-End"]
]

class Escolha:
    def __init__(self, tipo: TipoEscolha, opcao: str, caminho: str) -> None:
        self.tipo = tipo
        self.opcao = opcao
        self.caminho = caminho
        self.selecionada = None
    
    def selecionar(self):
        self.selecionada = True
        
    def pular(self):
        self.selecionada = False

def preencher_escolhas(escolhas: list):
    for escolha in escolhas:
        print(escolha.opcao + " ")
        try:
            opcao = int(input("1 - SIM / 2 - NÃO: "))
            if opcao == 1:
                escolha.selecionar()
            elif opcao == 2:
                escolha.pular()
            else: 
                raise Exception()
        except:
            print("Opção inválida")
            print("1 - SIM / 2 - NÃO: ")
            
def exibir_historia(escolhas: List[Escolha]):
    for escolha in escolhas:
        if escolha.selecionada:
            print(f"Você é {escolha.caminho}.")
        else:
             print(f"Você não é {escolha.caminho}.")

escolhas =[Escolha(historia[0], historia[1], historia[2]) for historia in criacao_historia]   
preencher_escolhas(escolhas)
exibir_historia(escolhas)