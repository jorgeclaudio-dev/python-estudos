print(
        '='*30,
        'Empréstimo Bancário'.center(30, " "),
        '='*30,
        sep='\n'
    )

casa = float(input('Valor da casa: R$ '))
salario = float(input('Qual salário do comprador: R$ '))
anos = int(input('Quantos anos: '))
tempo = anos * 12
prestacao = casa / tempo
limite = salario * (30/100)

print(f'A quantidade de prestações foram de {tempo} parcelas de R$ {prestacao:.2f} reais.')
print(f'Seu limite é de 30% do seu salário de R$ {salario:.2f} que foi R$ {limite:.2f}')

if prestacao > limite:
    print('Empréstimo negado')
else:
    print('Empréstimo aceito')