valor = float (input('Quanto você tem na carteira? '))
d = float (valor / 3.27)
print('Com R${} Você pode comprar US${:.2f} dolares'.format(valor,d))
