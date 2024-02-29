import random #ou import radint
lista = [0, 1, 2, 3, 4, 5] #ou pensar= radint(0, 5)
escolhido = random.choice(lista)
n = int (input('Adivinhe o número que o computador está pensando: '))
if n == escolhido:
    print('Você acertou, era nesse número que o computador estava pensando')
else:
    print('Você errou, não era esse número, era {}'.format(escolhido))
