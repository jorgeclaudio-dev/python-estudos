from datetime import datetime
data_atual = datetime.now().year
ano_nasc = int(input('Em que ano você nasceu: '))
idade = data_atual - ano_nasc

if idade < 1 or idade > 130:
    print('Digite um ano de nascimento válido')
elif idade < 18:
    maioridade = 18 - idade
    print(f'Você tem {idade} anos, faltam {maioridade} para se alistar')
elif idade == 18:
    print(f'Você tem {idade} anos, está no ano de se alistar guerreiro!')
else:
    atrasado = idade - 18
    print(f'Você tem {idade} anos, já passaram {atrasado} que você deveria ter se alistado!')