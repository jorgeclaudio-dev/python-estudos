aluno = str(input('Nome do aluno: '))
prova = float(input('Nota da prova: '))
trabalho = float(input('Nota do trabalho: '))
media = (prova + trabalho) / 2
print('-='*20)
print(f'Análise do(a) aluno(a) {aluno}\nNa prova {prova:.1f}\nNo trabalho {trabalho:.1f}\nA média foi de {media:.1f}')
print('-='*20)