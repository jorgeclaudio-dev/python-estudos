from math import ceil, floor

nome = input('Nome do(a) aluno(a): ')
prova = float(input('Nota da prova: '))
trabalho = float(input('Nota do trabalho: '))

if prova > 10 or prova < 0 or trabalho > 10 or trabalho < 0:
    print('-=' * 15)
    print('Notas INVÁLIDAS')
else:
    media = (prova + trabalho) / 2
    print('[ 1 ] Para bom aluno\n[ 2 ] Para mau aluno\n[  ] Outras números serão neutros')
    escolha = int(input('Resposta: '))
    if escolha == 1:
        notaReal = ceil(media)
    elif escolha == 2:
        notaReal = floor(media)
    else:
        notaReal = media
    print('-=' * 15)
    print(f'Aluno(a): {nome}\nProva: {prova}\nTrabalho: {trabalho}\nMedia: {notaReal}')
    print('-=' * 15)

    if media >=6:
        print(f'{nome} foi APROVADO(A)!')
    else:
        print(f'{nome} foi REPROVADO(A)!')
print('-=' * 15)
