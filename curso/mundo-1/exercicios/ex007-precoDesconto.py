precoProduto = float(input('Preço: R$ '))
descontoProduto = float(input('Desconto aplicado: '))
descontoAplicado = (precoProduto * descontoProduto) / 100
valorReal_Produto = precoProduto - descontoAplicado
print(f'O produto de R$ {precoProduto:.2f} com desconto de {descontoProduto}%\nFicou por R$ {valorReal_Produto:.2f}')