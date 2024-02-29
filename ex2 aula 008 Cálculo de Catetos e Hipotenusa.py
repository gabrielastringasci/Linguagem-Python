from calculadorafabeliz import basicOperations
from calculadorafabeliz import mathOperations
import math

c = basicOperations.calculadora()
o = mathOperations.otrasoperaciones ()

cateto_oposto = float(input("Digite o comprimento do cateto oposto: "))
cateto_adjacente = float(input("Digite o comprimento do cateto adjacente: "))

print('Hipotenusa: ', math.floor(o.hipotenusa(cateto_oposto, cateto_adjacente)))