"""
    Neste exercício, você deverá escrever um programa em Python que verifique se um número fornecido pelo usuário é par ou ímpar. 
    Imprima uma mensagem indicando se o número é par ou ímpar.
"""

from enum import Enum


class ClassificacaoNumero(Enum):
    PAR = 1
    IMPAR = 2

def obter_numero() -> int:
    while True:
        try:
            numero = int(input("Número Inteiro: "))
            return numero
        except:
            print("Número inválido.")

def classificar_numero(numero: int) -> ClassificacaoNumero:
    if numero % 2 == 0: return ClassificacaoNumero.PAR
    return ClassificacaoNumero.IMPAR

numero = obter_numero()
classificacao_numero = classificar_numero(numero)
resposta = "Par" if classificacao_numero == ClassificacaoNumero.PAR else "Ímpar"
print(f"O número \"{numero}\" é {resposta}")