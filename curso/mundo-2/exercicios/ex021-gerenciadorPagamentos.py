print(
    '='*40,
    'Gerenciador de Pagamentos'.center(40, " "),
    '[ 1 ] Dinheiro / Cheque: desconto 10%',
    '[ 2 ] À vista cartão: desconto 5%',
    '[ 3 ] 2x no cartão: sem desconto',
    '[ 4 ] 3x ou mais no cartão: juros de 20%',
    '='*40,
    sep='\n'
)
preco_normal = float(input('Preço do produto: R$ '))
opcao = int(input('Qual a opção de pagamento: '))

if opcao < 1 or opcao > 4:
    print('Opção inválida!')
elif opcao == 1:
    desconto = preco_normal * (10 / 100)
    preco = preco_normal - desconto
    print(f'Preço Original R$ {preco_normal:.2f}\nDesconto de 10%: R$ {desconto:.2f}\nPreço Atual R$ {preco:.2f}')
elif opcao == 2:
    desconto = preco_normal * (5 / 100)
    preco = preco_normal - desconto
    print(f'Preço Original R$ {preco_normal:.2f}\nDesconto de 5%: R$ {desconto:.2f}\nPreço Atual R$ {preco:.2f}')
elif opcao == 3:
    print(f'Preço: R$ {preco_normal:.2f}')
else:
    juros = preco_normal * (20 / 100)
    preco = preco_normal + juros
    print(f'Preço Original R$ {preco_normal:.2f}\nJuros de 20%: R$ {juros:.2f}\nPreço Atual R$ {preco:.2f}')