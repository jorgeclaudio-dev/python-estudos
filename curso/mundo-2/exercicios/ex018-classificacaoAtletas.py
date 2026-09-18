from datetime import datetime
ano_atual = datetime.now().year
ano_nasc = int(input('Em que ano o atleta nasceu: '))
idade = ano_atual - ano_nasc

if ano_nasc > ano_atual or ano_nasc < (ano_atual - 130):
    print('Ano de nascimento inválido!')
elif idade <= 9:
    print(f'Idade: {idade} anos\nAtleta: MIRIM!')
elif idade <= 14:
    print(f'Idade: {idade} anos\nAtleta: INFANTIL!')
elif idade <= 19:
    print(f'Idade: {idade} anos\nAtleta: JUNIOR!')
elif idade == 20:
    print(f'Idade: {idade} anos\nAtleta: SENIOR!')
else:
    print(f'Idade: {idade} anos\nAtleta: MASTER!')