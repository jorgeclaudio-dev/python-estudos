larg = float(input('Largura da parede em metros: '))
comp = float(input('Comprimento da parede em metros: '))
area = larg * comp
tinta = area / 2
print(f'Uma parede de {area:.2f}m² precisa de {tinta}L de tinta')