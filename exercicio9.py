"""
    Desenvolva um programa que aplique descontos progressivos com base no valor da compra: desconto de 10% 
        para compras acima de R$100, 15% para compras acima de R$200, seguindo a projeção até R$500, 
        para valores maiores do que esse, o desconto é fixado em 25%.
"""

def obter_valor_compra() -> float:
    while True:
        try:
            valor_compra = float(input("Informe o valor da compra: "))
            
            if (valor_compra <= 0): raise Exception("Valor inválido")
            
            return valor_compra
        except:
            print("Valor inválido")
            
def obter_desconto(valor_compra: float) -> float:
    """ Retorna desconto em porcentagem => Ex: 10% = 0.1, 15% = 0.15, 25% = 0.25 """
    if valor_compra > 100: return 0.1
    elif valor_compra > 200 and valor_compra <= 500: return 0.15
    elif valor_compra > 500: return 0.25
    else: return 0
    
def exibir_desc
    