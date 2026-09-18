peso = float(input('Qual peso: '))
altura = float(input('Qual a altura: '))
imc = peso / (altura ** 2)
print(f'Seu IMC é: {imc:.1f}')

if imc < 18.5:
    print('Abaixo do peso.')
elif imc < 25:
    print('Peso ideal.')
elif imc < 30:
    print('Sobrepeso.')
elif imc < 40:
    print('Obesidade.')
else:
    print('Obesidade Mórbida.')
