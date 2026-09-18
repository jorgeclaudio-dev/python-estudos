import random
from time import sleep
opcoes = ["Pedra", "Papel", "Tesoura"]
pc_opcao = random.choice(opcoes)
print(
    '='*30,
    'Pedra, Papel e Tesoura!'.center(30, " "),
    '[ 1 ] Para pedra',
    '[ 2 ] Para papel',
    '[ 3 ] Para tesoura',
    '='*30,
    sep='\n'
)
user_opcao = input('Qual sua jogada: ')
user_jogada = {
        "1": "Pedra",
        "2": "Papel",
        "3": "Tesoura"
    }
escolha = user_jogada.get(user_opcao)

if escolha:

    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!')
    sleep(1)
    print('='*30)
    print(f'PC: {pc_opcao}\nUser: {escolha}')

    if escolha == pc_opcao:
        print('EMPATE!')
    elif (
        (escolha == "Pedra" and pc_opcao == "Tesoura")
        or (escolha == "Papel" and pc_opcao == "Pedra")
        or (escolha == "Tesoura" and pc_opcao == "Papel")
    ):
        print("JOGADOR VENCE!")
    else:
        print('Jogador Perde!')

else:
    print('OPÇÃO INVÁLIDA!')
