salario=float(input('Digite o salário do funcionário: '))
aumento=15
aumento2=float(aumento / 100) * salario
final= float (salario+aumento2)
print('O aumento foi de {}% = R${:.2f} e o salário final é: R${:.2f}'.format(aumento, aumento2,final))
