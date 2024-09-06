"""
    Crie um programa que apresente ao usuário uma série de escolhas (como em uma história) 
        e conduza a diferentes resultados com base nessas escolhas.
"""

class Escolha:
    def __init__(self, opcao: str) -> None:
        self.opcao = opcao
        self.selecionada = None
    
    def selecionar(self):
        self.selecionada = True
        
    def pular(self):
        self.selecionada = False

opcoes = [
    "Você é programador?", 
    "Você estuda TI?", 
    "Você quer ser Front-End?", 
    "Você quer ser Back-End?"
]

escolhas = [Escolha(opcao) for opcao in opcoes]

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
    