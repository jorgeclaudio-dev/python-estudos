A = float(input('Primeiro segmento mede: '))
B = float(input('Segundo segmento mede: '))
C = float(input('Terceiro segmento mede: '))

if A + B > C and A + C > B and B + C > A:
    print('Pode ser um triângulo!')
    if A == B and B == C:
        print('Triângulo Equilátero!')
    elif A == B or B == C or A == C:
        print('Triângulo Isósceles!')
    else:
        print('Triângulo Escaleno!')