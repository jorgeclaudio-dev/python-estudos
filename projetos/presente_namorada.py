from datetime import datetime
from dateutil.relativedelta import relativedelta

# Datas importantes do relacionamento

agora = datetime.now() # Data e hora atual
data_conhecemos = datetime(2025, 4, 7) # Dia que nos conhecemos
data_namoro = datetime(2025, 9, 7) # Dia que pedi ela em namoro

# Calculo do tempo em que a conheci e que namoramos

tempo_conhecemos = relativedelta(agora, data_conhecemos)
tempo_namoro = relativedelta(agora, data_namoro)

# Função de tempo
def calcular_tempo(tempo):
    partes = []
    if tempo.years > 0:
        if tempo.years > 1:
            partes.append(f'{tempo.years} anos')
        else:
            partes.append('1 ano')
    if tempo.months > 0:
        if tempo.months > 1:
            partes.append(f'{tempo.months} meses')
        else:
            partes.append('1 mês')
    if tempo.days > 0:
        if tempo.days > 1:
            partes.append(f'{tempo.days} dias')
        else:
            partes.append('1 dia')
    if len(partes) == 1:
        return partes[0]
    elif len(partes) > 1:
        contagem = ", ".join(partes[:-1]) + " e " + partes[-1]
        return contagem
    else:
        return 'Quantidade de tempo inconsistente'

contagem_conhecemos = calcular_tempo(tempo_conhecemos)
contagem_namoro = calcular_tempo(tempo_namoro)

print(f"Nos conhecemos há {contagem_conhecemos}.")
print(f"Namoramos há {contagem_namoro}.")
