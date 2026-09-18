numero = int(input('Escolha um número inteiro: '))
print(
    '='*30,
    'Conversor Númerico'.center(30, " "),
    '='*30,
    '[ 1 ] para binário',
    '[ 2 ] para octal',
    '[ 3 ] para hexadecimal',
    '[ 4 ] para sair',
    '='*30,
    f'Número escolhido {numero}',
    sep='\n'
)
opcao = int(input('Escolha entre as opções acima: '))

if opcao > 4 or opcao < 1:
    print('Opção inválida')
    exit()
elif opcao == 1:
    print(f'{numero} convertido em binário é {bin(numero)[2:]}')
elif opcao == 2:
    print(f'{numero} convertido em octal é {oct(numero)[2:]}')
elif opcao == 3:
    print(f'{numero} convertido em hexadecimal é {hex(numero)[2:]}')
else:
    print('Saindo do sistema...')
    exit()