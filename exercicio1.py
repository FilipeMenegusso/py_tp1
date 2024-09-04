""" 
	Crie um programa que peça ao usuário para inserir dois números e, em seguida, 
    calcule e exiba a soma, subtração, multiplicação, divisão e divisão inteira desses números.
"""

def obter_numero(legenda: str) -> float:
	""" Retorna um número válido digitado pelo usuário """
	while True:
		try:
			return float(input(legenda))
		except:
			print("Número Inválido.")

def exibir_soma(numero1: float, numero2: float) -> None:
	soma = numero1 + numero2
	print(f"Soma => {numero1} + {numero2} = {soma}")

def exibir_subtracao(numero1: float, numero2: float) -> None:
	""" Exibe a subtração de 2 números """
	subtracao = numero1 - numero2
	print(f"Subtração => {numero1} - {numero2} = {subtracao}")
	
def exibir_multiplicacao(numero1: float, numero2: float) -> None:
	""" Exibe a multiplicação de 2 números """
	produto = numero1 * numero2
	print(f"Produto => {numero1} * {numero2} = {produto}")

def exibir_divisao(numero1: float, numero2: float) -> None:
	""" Exibe a divisão de 2 números """
	divisao = numero1 / numero2
	print(f"Divisão => {numero1} / {numero2} = {divisao}")

def exibir_divisao_inteira(numero1: float, numero2: float) -> None:
	""" Exibe a divisão inteira de 2 números """
	divisao = numero1 // numero2
	print(f"Divisão Inteira => {numero1} // {numero2} = {divisao}")

numero1 = obter_numero("Número 1: ")
numero2 = obter_numero("Número 2: ")
exibir_soma(numero1, numero2)
exibir_subtracao(numero1, numero2)
exibir_multiplicacao(numero1, numero2)
exibir_divisao(numero1, numero2)
exibir_divisao_inteira(numero1, numero2)
