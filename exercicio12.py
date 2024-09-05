"""
    Crie um programa que classifique as palavras inseridas pelo usuário como curtas (menos de 5 letras) 
    ou longas (5 letras ou mais).
"""

from enum import Enum

class ClassificacaoPalavra(Enum):
    CURTA = 1
    LONGA = 2

class ClassificadorPalavras:
    """
        Classifica e exibe se uma palavra é LONGA ou CURTA
    """
    
    def __init__(self) -> None:
        self.QTD_CARACTERES_PALAVRA_LONGA = 5
        
    def classificar_palavra(self, palavra: str) -> ClassificacaoPalavra:
        if len(palavra) >= self.QTD_CARACTERES_PALAVRA_LONGA: return ClassificacaoPalavra.LONGA
        return ClassificacaoPalavra.CURTA
    
    def exibir_classificacao_palavra(self, palavra: str):
        classificacao = self.classificar_palavra(palavra)
        descricacao_classificacao = "LONGA" if classificacao == ClassificacaoPalavra.LONGA else "CURTA"
        print(f"A palavra \"{palavra}\" é {descricacao_classificacao}")
    
def obter_palavra() -> str:
    while True:
        try:
            palavra = input("Informa 1 palavra: ")
            return palavra
        except:
            print("Palavra inválida")
            
palavra = obter_palavra()
classificador = ClassificadorPalavras()
classificador.exibir_classificacao_palavra(palavra)
