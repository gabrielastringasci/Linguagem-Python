vel = int (input('Qual a velocidade atual do carro? '))
if vel > 80:
    multa = (vel-80)*7
    print('Você está acima do limite de velocidade permitido e foi multado! O valor da multa é: R${:.2f}.'.format(multa))
else:
    print('Você está dentro do limite de velocidade permitido')