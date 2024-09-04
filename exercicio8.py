"""
    Crie um programa que pergunte a idade do usuário e verifique se ele é maior de idade ou não.
"""

def obter_idade() -> int:
    while True:
        try:
            idade = int(input("Informe a sua idade: "))
            
            if idade <= 0: raise Exception("Idade inválida")
            
            return idade
        except:
            print("Idade inválida")
            
def validar_maioridade(idade):
    MAIORIDADE = 18
    if (idade >= MAIORIDADE): print("Maior de idade")
    else: print("Menor de idade")
    
idade = obter_idade()
validar_maioridade(idade)