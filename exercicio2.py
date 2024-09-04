"""
    Faça um programa que converta um número fornecido de minutos em horas e minutos, e depois faça o inverso, 
    convertendo horas e minutos de volta para minutos totais.
"""

class Tempo:
    def __init__(self, horas, minutos) -> None:
        self.horas = horas
        self.minutos = minutos
        # self.minutos = minutos
        # self.minutos_totais = minutos

def obter_minutos_totais() -> int:
    """ Retorna minutos válidos digitados pelo usuário """
    while True:
        try:
            return int(input("Digite os minutos: "))
        except:
            print("Minutos Inválidos.")

def obter_tempo_horas_minutos_de_minutos_totais(minutos_totais: int) -> Tempo:
    """ Retorna um objeto do tipo Tempo que possui hora e minutos convertidos """
    horas = minutos_totais // 60
    minutos = minutos_totais % 60
    return Tempo(horas, minutos)
    
def converter_tempo_para_minutos_totais(tempo: Tempo) -> int:
    """ Converte Tempo(Horas + Minutos) para minutos totais """
    minutos_totais = (tempo.horas * 60) + tempo.minutos
    return minutos_totais
    
minutos_totais = obter_minutos_totais()
    
tempo = obter_tempo_horas_minutos_de_minutos_totais(minutos_totais)
print(f"{minutos_totais}m -> {tempo.horas}h:{tempo.minutos}m")
    
minutos_totais_convertidos = converter_tempo_para_minutos_totais(tempo)
print(f"{tempo.horas}h:{tempo.minutos}m -> {minutos_totais_convertidos}m")
