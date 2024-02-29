salario = float(input('Qual seu salario? '))
if salario <= 1250:
    porcentagem = (salario/100) * 15
    aumento = porcentagem + salario
    print ('Seu aumento foi de 15% (R${:.2f}) e seu novo salário é: R${:.2f}'.format(porcentagem, aumento))
else:
    porcentagem1 = (salario/100) * 10
    aumento1 = porcentagem1 + salario
    print ('Seu aumento foi de 10% (R${:.2f}) e seu novo salário é: R${:.2f}'.format(porcentagem1, aumento1))