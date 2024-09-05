"""
    Escreva um programa que combine elementos aleatórios de listas diferentes (personagens, ações, locais) 
    para criar uma história curiosa.
"""

import random


def gerar_historia(personagens: list, acoes: list, locais: list) -> list:
    """
        Gera um história aleatória a partir de personagens, ações e locais
    """
    historia = []
    
    historia.extend(personagens.copy())
    historia.extend(acoes.copy())
    historia.extend(locais.copy())
    random.shuffle(historia)
    return historia

personagens = [
    "Luffy",
    "Franky",
    "Supernovas",
    "Nami",
    "Brooke",
    "Portgas D. Ace",
    "Nico Robin",
    "Edward Newgate",
    "Enel",
    "Roronoa Zoro",
    "Yonkou",
    "Tashigi",
    "Cobby",
    "Rob Lucci",
    "Buggy",
    "o Palhaço",
    "Aokiji",
    "Oimo",
    "Kashi",
    "Helmeppo",
    "Smoker",
    "Monkey D."
]

acoes = [
    "Gomu Gomu no Elephant Gun.",
    "Gomu Gomu no Elephant Gatling.",
    "Gomu Gomu no Grizzly Magnum.",
    "Gomu Gomu no Kong Gun.",
    "Gomu Gomu no Rhino Schneider.",
    "Gomu Gomu no King Kong Gun.",
    "Gomu Gomu no Kong Organ.",
    "Gomu Gomu no Black Mamba.",
    "Haoshoku Haki"
]

locais = [
    "East blue",
    "West Blue",
    "North Blue",
    "South Blue",
    "Red Line",
    "Calm Belt",
    "Grand Line",
    "Novo Mundo",
    "Oceanos Celestes",
    "Mar Branco",
    "Mar Branco-Branco",
    "Outros",
    "Mar Subterrâneo",
    "Lua",
    "No East Blue",
    "Grand Line",
    "Paraíso",
    "Novo Mundo"
]

historia = gerar_historia(personagens, acoes, locais)

for parte_historia in historia:
    print(parte_historia)