salario = int(input('Qual o salário:  '))


if salario > 1250.00:
    aumento=salario*1.10
    perc=10
else:
    aumento=salario*1.15
    perc=15

print('O seu salario de R$ {:,.2f}  com o aumento de {}% vai ser R${:,.2f}'.format(salario,perc,aumento))