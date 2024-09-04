"""
    Escreva um programa onde o usuário deve adivinhar um número secreto. 
    O programa deve dizer se o palpite está correto, muito alto ou muito baixo.
"""
from random import random


def gerar_numero_secreto() -> int:
    return int(random() * 100)

def obter_palpite() -> int:
    while True:
        try:
            palpite = int(input("Qual é o seu palpite (Número Inteiro)? "))
            return palpite
        except:
            print("Palpite (Número Inteiro) inválido")

def adivinhar_numero_secreto(numero_secreto: int):
    PORCENTAGEM_PALPITE_MUITO_ALTO = 1.5
    PORCENTAGEM_PALPITE_MUITO_BAIXO = 0.1
    
    while True:
        palpite = obter_palpite()
        if (palpite == numero_secreto):
            print(f"Palpite correto: {palpite}")
            return
        else:
            porcentagem_palpite = palpite / numero_secreto
            if porcentagem_palpite >= PORCENTAGEM_PALPITE_MUITO_ALTO:
                print("Palpite muito alto")
            elif porcentagem_palpite <= PORCENTAGEM_PALPITE_MUITO_BAIXO:
                print("Palpite muito baixo")
            elif palpite > numero_secreto:
                print("Palpite alto")
            else: 
                print("Palpite baixo")
                
numero_secreto = gerar_numero_secreto()
adivinhar_numero_secreto(numero_secreto)
    