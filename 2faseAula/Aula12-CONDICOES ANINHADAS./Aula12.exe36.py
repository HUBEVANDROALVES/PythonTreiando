valorcasa = int(input('Digite o valor da casa: '))
salario = int(input('Digite salario: '))
prazo = int(input('Quantos anos para paga? '))
prest = valorcasa/prazo*12

if salario*0.30 > prest :
   print('Seu financiamento nao foi aprovado\n abaixo do valor minimo')
else:
    print('seu financiamento foi aprovado \nrenda suficiente')



