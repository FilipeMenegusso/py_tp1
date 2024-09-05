"""
    Desenvolva um programa que aplique descontos progressivos com base no valor da compra: desconto de 10% 
        para compras acima de R$100, 15% para compras acima de R$200, seguindo a projeção até R$500, 
        para valores maiores do que esse, o desconto é fixado em 25%.
"""

def obter_desconto(valor_compra: float) -> float:
    """ Retorna desconto em porcentagem => Ex: 10% = 0.1, 15% = 0.15, 25% = 0.25 """
    if valor_compra > 100 and valor_compra <= 200: return 0.1
    elif valor_compra > 200 and valor_compra <= 500: return 0.15
    elif valor_compra > 500: return 0.25
    else: return 0
class Compra:
    """ Recebe o valor de compra e deixa clculado o desconto """
    def __init__(self, valor_compra: float):
        self.valor_compra = valor_compra
        self.porcentagem_desconto = obter_desconto(self.valor_compra)
        self.desconto_formatado = self.porcentagem_desconto * 100
        self.valor_total_com_desconto = (1 - self.porcentagem_desconto) * self.valor_compra
                
    def exibir_desconto_e_valor_compra(self):
        """ 
            Exibe o desconto aplicado no valor de compra 
            Valor da compra: R$300
            Valor com desconto de 30%: R$270
        """
        
        print(f"Valor da compra: R${self.valor_compra}")
        
        if self.porcentagem_desconto > 0: 
            print(f"Valor com desconto de {self.desconto_formatado}%: {self.valor_total_com_desconto}")

def obter_valor_compra() -> float:
    """ Obtém um valor de compra válido informa pelo usuário """
    while True:
        try:
            valor_compra = float(input("Informe o valor da compra: "))
            
            if (valor_compra <= 0): raise Exception("Valor inválido")
            
            return valor_compra
        except:
            print("Valor inválido")
            
compra_usuario = obter_valor_compra()
compras = [Compra(compra_usuario), Compra(100), Compra(101), Compra(200), Compra(300), Compra(501)]
for compra in compras:
    compra.exibir_desconto_e_valor_compra()
    print()
    
    

    



    