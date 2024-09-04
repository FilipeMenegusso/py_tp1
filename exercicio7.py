"""
    Faça um programa que calcule o Índice de Massa Corporal (IMC) do usuário 
    e forneça feedback com base no valor (por exemplo, abaixo do peso, peso normal, sobrepeso).
"""

import math

def calcular_imc(peso: float, altura: float) -> float:
    """ Retorna o IMC =>  peso/(altura x altura) """
    return math.ceil(peso / (altura * altura))

def exibir_resultado_imc(imc: float) -> str:
    """ 
        Resultado do IMC: abaixo do peso, peso normal, sobrepeso
        IMC < 18,5 - abaixo do peso
        IMC > 18,5 até 24,9 - peso normal 
        IMC >= 25 - sobrepeso
    """
    if imc <= 18.5:
        print(f"IMC {imc}: abaixo do peso")      
    elif imc > 18.5 and imc <= 24.9:
        print(f"IMC {imc}: peso normal")   
    elif imc >= 25:
        print(f"IMC {imc}: sobrepeso")

def obter_peso() -> float:
    while True:
        try:
            peso = float(input("Digite seu peso: "))
            
            if (peso <= 0):
                raise Exception("Peso inválido")
            
            return peso
        except:
            print("Peso inválido")
            
def obter_altura() -> float:
    while True:
        try:
            altura = float(input("Digite sua altura: "))
            
            if (altura <= 0):
                raise Exception("Altura inválida")
            
            return altura
        except:
            print("Altura inválida")
            
peso = obter_peso()
altura = obter_altura()
imc = calcular_imc(peso, altura)
exibir_resultado_imc(imc)