import random

n1=input('Digite o nome do primeiro grupo: ')
n2=input('Digite o nome do segundo grupo: ')
n3=input('Digite o nome do terceiro grupo: ')
n4=input('Digite o nome do quarto grupo: ')

grupos=[n1,n2,n3,n4]

random.shuffle(grupos)

print('Ordem da apresentação: ')
print(grupos)
