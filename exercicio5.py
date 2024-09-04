"""
    Crie um programa que peça ao usuário seu nome e sobrenome usando input e, em seguida, 
    combine-os para formar uma saudação personalizada.
"""

def obter_texto(legenda: str) -> str:
    """ Retorna um texto não vazio """
    while True:
        try:
            texto = input(legenda)
            if texto.strip() == "": print(f"\"{legenda}\" vazio")
            else: return texto
        except:
            print("Texto inválido.")
            
def exibir_saudacao(nome: str, sobrenome: str) -> None:
    print(f"Olá {nome} {sobrenome}")
            
nome = obter_texto("Nome: ")
sobrenome = obter_texto("Sobrenome: ")

exibir_saudacao(nome, sobrenome)