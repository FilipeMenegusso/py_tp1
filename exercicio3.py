"""
    Escreva um programa que receba dois nomes de usuário e os combine de maneira criativa para formar um novo nome.
"""

def obter_nome() -> str:
    while True:
        try:
            nome = input("Nome: ")
            if (nome.strip() == ""): continue
            return nome
        except:
            print("Nome inválido.")
            
def concatenar_nomes(nome1: str, nome2: str) -> str: 
    """ Concatena 2 nomes separando-os por espaço """
    return f"{nome1} {nome2}"
            
nome1 = obter_nome()
nome2 = obter_nome()
nome_completo = concatenar_nomes(nome1, nome2)
print(nome_completo)