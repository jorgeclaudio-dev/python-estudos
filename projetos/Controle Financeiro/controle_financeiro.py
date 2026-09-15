import json
from datetime import datetime
def carregar_lancamentos():
    with open('lancamentos.json', 'r') as arquivo:
        lancamentos = json.load(arquivo)
        return lancamentos
def salvar_lancamentos():
    with open('lancamentos.json', 'w') as arquivo:
        json.dump(lancamentos, arquivo, indent=4)
def proximo_id():
    if not lancamentos:
        return 1

    return max(item['id'] for item in lancamentos) + 1
def adicionar_lancamento(tipo):
    descricao = input('Descrição: ').strip()
    if not descricao:
        print('A descrição não pode ficar vazia.')
        return
    try:
        valor = float(input('Valor: '))
    except ValueError:
        print('Digite apenas números')
        return
    if valor <= 0:
        print('O valor deve ser maior que zero.')
        return

    data_atual = datetime.now().strftime('%d/%m/%Y')
    data = input(f'Data [{data_atual}]: ').strip()
    if not data:
        data = data_atual

    try:
        datetime.strptime(data, '%d/%m/%Y')
    except ValueError:
        print('Data inválida. Use o formato DD/MM/AAAA')
        return

    id_lancamento = proximo_id()

    novo_lancamento = {
        "id": id_lancamento,
        "descricao": descricao,
        "valor": valor,
        "tipo": tipo,
        "data": data
    }
    lancamentos.append(novo_lancamento)
    salvar_lancamentos()
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
            print(f"° {item['id']:<4} | {item['data']:<12} | {item['descricao']:<15} | R$ {item['valor']:>8.2f} | {item['tipo']}")
def excluir_lancamento():
    try:
        id_lancamento = int(input('Digite o ID do lançamento que deseja excluír: '))
    except ValueError:
        print('Digite apenas números.')
        return
    if not any(item['id'] == id_lancamento for item in lancamentos):
        print('Lançamento não encontrado.')
        return
    for item in lancamentos:
        if item['id'] == id_lancamento:
            lancamentos.remove(item)
    salvar_lancamentos()

def editar_lancamento():
    try:
        id_lancamento = int(input('Digite o ID: '))
    except ValueError:
        print('Digite apenas números.')
        return
    if not any(item['id'] == id_lancamento for item in lancamentos):
        print('Lançamento não encontrado.')
        return
    for item in lancamentos:
        if item['id'] == id_lancamento:
            print(
                'Lançamento encontrado:',
                f"Descrição: {item['descricao']}",
                f"Valor: R${item['valor']:.2f}",
                sep='\n'
            )
            nova_descricao = input('Descrição: ').strip()
            if not nova_descricao:
                print('A descrição não pode ficar vazia.')
                return
            try:
                novo_valor = float(input('Valor: R$ '))
            except ValueError:
                print('Digite apenas números.')
                return
            if novo_valor <= 0:
                print('O valor deve ser maior que zero.')
                return
            item['descricao'] = nova_descricao
            item['valor'] = novo_valor
            print('Lançamento editado com sucesso.')
    salvar_lancamentos()

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
lancamentos = carregar_lancamentos()
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
        '5 - Excluír lançamento',
        '6 - Editar lançamento',
        '0 - Sair',
        sep='\n'
    )
    try:
        opcao = int(input('Escolha uma opção: '))
    except ValueError:
        print('Digite apenas números.')
        continue

    if opcao > 6 or opcao < 0:
        print('Opção Inválida.')
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

    elif opcao == 5:
        excluir_lancamento()

    elif opcao == 6:
        editar_lancamento()

    else:
        print('Saindo do sistema...')
        break