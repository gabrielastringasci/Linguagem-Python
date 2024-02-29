from calculadorafabeliz import basicOperations
from calculadorafabeliz import mathOperations

o = mathOperations.otrasoperaciones ()
c = basicOperations.calculadora ()

angulo = float(input('Digite um ângulo: '))

print ( 'Seno: {:.3f}' .format(o.seno (angulo)))
print ( 'Coseno: {:.3f}' .format(o.coseno (angulo)))
print ( 'Tangente: {:.3f}' .format(o.tangente (angulo)))