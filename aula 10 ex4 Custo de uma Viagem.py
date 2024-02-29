distancia = float(input('Qual a distancia da viagem em KM? '))
if distancia <= 200:
    valorp = distancia * 0.50
    print ('Para essa distancia o valor da passagem é R${:.2f}'.format(valorp))
else:
    valorp1= distancia * 0.45
    print('Para essa distancia o valor da passagem é R${:.2f}'.format(valorp1))