nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2

if nota1 > 10 or nota1 < 0 or nota2 > 10 or nota2 < 0:
    print('Notas inválidas!')
elif media < 5:
    print(f'Média: {media}\nReprovado!')
elif media < 7:
    print(f'Média: {media}\nRecuperação!')
else:
    print(f'Média: {media}\nAprovado!')
