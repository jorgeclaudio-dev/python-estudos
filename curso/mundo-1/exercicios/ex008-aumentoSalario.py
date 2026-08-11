salarioAtual = float(input('Salário atual do funcionário: R$ '))
aumentoSalario = float(input('Aumento de: '))
salarioAumento = salarioAtual + ((salarioAtual * aumentoSalario) / 100)
print(f'O sálario de R$ {salarioAtual:.2f} com {aumentoSalario}% ficou R$ {salarioAumento:.2f}')