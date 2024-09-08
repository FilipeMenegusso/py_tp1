"""
    Desenvolva um programa que peça ao usuário para escolher uma operação (adição, subtração, multiplicação, divisão) e dois números, 
    e então execute a operação escolhida com os números.
"""

from enum import Enum

class Operacao(Enum):
    ADICAO = 1
    SUBTRACAO = 2
    MULTIPLICACAO = 3
    DIVISAO = 4

def obter_numero(legenda: str) -> float:
	""" Retorna um número válido digitado pelo usuário """
	while True:
		try:
			return float(input(legenda))
		except:
			print("Número Inválido.")
   
def obter_operacao() -> Operacao:
    while True:
        try:
            operacao = int(input("Digite uma operação: 1 (Adição), 2 (Subtração), 3 (Multiplicação), 4 (Divisão): "))
            return Operacao(operacao)
        except:
            print("Operação inválida")

def calcular_operacao(operacao: Operacao, numero1: float, numero2: float) -> float:
    """ Retorna o resultado da operação entre 2 números """
    if (operacao == Operacao.ADICAO): return numero1 + numero2
    if (operacao == Operacao.SUBTRACAO): return numero1 - numero2
    if (operacao == Operacao.MULTIPLICACAO): return numero1 * numero2
    if (operacao == Operacao.DIVISAO): return numero1 / numero2
    
def exibir_resultado_operacao(operacao, numero1, numero2, resultado) -> None:
    sinal_operacao = ""
    nome_operacao = ""
    
    if (operacao == Operacao.ADICAO): 
        sinal_operacao = "+"
        nome_operacao = "Adição"
    elif (operacao == Operacao.SUBTRACAO): 
        sinal_operacao = "-"
        nome_operacao = "Subtração"
    elif (operacao == Operacao.MULTIPLICACAO): 
        sinal_operacao = "*"
        nome_operacao = "Multiplicação"
    elif (operacao == Operacao.DIVISAO):
        sinal_operacao = "/"
        nome_operacao = "Divisão"
    
    print(f"{nome_operacao} -> {numero1} {sinal_operacao} {numero2} = {resultado}")
    
    
operacao = obter_operacao()
numero1 = obter_numero("Número 1: ")
numero2 = obter_numero("Número 2: ")
resultado = calcular_operacao(operacao, numero1, numero2)
exibir_resultado_operacao(operacao, numero1, numero2, resultado)
    