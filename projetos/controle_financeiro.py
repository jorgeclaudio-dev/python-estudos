lancamentos = []
def adicionar_lancamento(tipo):
    descricao = input('Descrição: ')
    valor = float(input('Valor: '))
    novo_lancamento = {
        "descricao": descricao,
        "valor": valor,
        "tipo": tipo
    }
    lancamentos.append(novo_lancamento)
def listar_lancamentos():
    if not lancamentos:
        print('Não possui lançamentos ainda.')
    else:
        print(
            '=' * 30,
            'TODOS OS LANÇAMENTOS'.center(30, ' '),
            '=' * 30,
            sep='\n'
        )
        for item in lancamentos:
            print(f"° {item['descricao']:<15} | R$ {item['valor']:>8.2f} | {item['tipo']}")
def calcular_saldo():
    total_receitas = 0
    total_despesas = 0
    for item in lancamentos:
        if item['tipo'] == 'receita':
            total_receitas += item['valor']
        else:
            total_despesas += item['valor']
    saldo = total_receitas - total_despesas
    return total_receitas, total_despesas, saldo
def mostrar_saldo():
    total_receitas, total_despesas, saldo = calcular_saldo()
    print(
        '=' * 30,
        'RESUMO DO SALDO'.center(30, ' '),
        '=' * 30,
        sep='\n'
    )
    print(
        f'Total de Receitas: R$ {total_receitas:.2f}',
        f'Total de Despesas: R$ {total_despesas:.2f}',
        '=' * 30,
        f'Saldo Atual:         R$ {saldo:.2f}',
        sep='\n'
    )
while True:
    print('\n')
    print(
        '='*30,
        'CONTROLE FINANCEIRO'.center(30, " "),
        '='*30,
        sep='\n'
    )
    print(
        '1 - Adicionar receita',
        '2 - Adicionar despesa',
        '3 - Listar lançamentos',
        '4 - Ver saldo',
        '0 - Sair',
        sep='\n'
    )
    opcao = int(input('Escolha uma opção: '))

    if opcao > 4 or opcao < 0:
        print(
            '=' * 30,
            'OPÇÃO INVÁLIDA'.center(30, ' '),
            '=' * 30,
            sep='\n'
        )
        continue

    elif opcao == 1 or opcao == 2:
        if opcao == 1:
            adicionar_lancamento('receita')
        else:
            adicionar_lancamento('despesa')

    elif opcao == 3:
        listar_lancamentos()

    elif opcao == 4:
        mostrar_saldo()
    else:
        print('Saindo do sistema...')
        break