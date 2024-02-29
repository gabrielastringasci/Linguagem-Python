preço = float(input('Digite o preço do produto: '))
descontoporcento = float(5)
desconto = float (descontoporcento / 100) * preço
final= float (preço-desconto)
print('Com o desconto de R${:.2F} o valor final a ser pago é: R${:.2f}'.format(desconto, final))
