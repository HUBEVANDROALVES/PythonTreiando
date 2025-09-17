from datetime import date

atual = date.today().year
demaior=0
demenor=0
qtd=int(input( 'Digite o numero de pessoa: '))
for i in range(qtd):
    nasc = int(input( 'Digite o ano de nascimento da {}º pessoa '.format(i+1)))
    idade = atual - nasc
    print('Essa pessoa tem {} Anos'.format(idade))
    if idade >= 21:
        demaior += 1
    else:
        demenor += 1

print('Temos {} pessoas de maior e {} de menor'.format(demaior,demenor))