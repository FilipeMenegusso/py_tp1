"""
    Escreva um programa que permita ao usuário votar em três opções diferentes e, no final, 
    exiba o número de votos de cada opção.
"""

class VotoOpcao:
    def __init__(self, opcao: str) -> None:
        self.opcao = opcao
        self.votos = 0
        
    def votar(self):
        while True:
            try: 
                self.votos = int(input(f"Votos para {self.opcao}: "))
                break
            except:
                print("Valor inválido")
        
    def exibir_votos(self):
        print(f"Votos da opção \"{self.opcao}\": {self.votos}")

OPCOES_ALIMENTOS = ["ARROZ", "FEIJÃO", "SALADA"]
opcoes = [VotoOpcao(opcao) for opcao in OPCOES_ALIMENTOS]

for opcao in opcoes:
    opcao.votar()
    
for opcao in opcoes:
    opcao.exibir_votos()



