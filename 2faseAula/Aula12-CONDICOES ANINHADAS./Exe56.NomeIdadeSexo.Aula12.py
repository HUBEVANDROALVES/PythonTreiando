import math
from datetime import datetime
qtd=0
mulher = ''
velho = 0
idadeJovem=0
media=0
idade1=0
idadev = 0
mulhernova = 0
nomevelho = ''
qtd = int(input( 'Digite a quatidade de pessoas \n    para a pesquisa:  ' ))
for i in range(qtd):
    nome=input( f'Digite o nome da {i+1}º pessoa: ')
    sexo=input( 'Digite o  sexo  M-masculino e F-feminino: ').upper()
    idade=int(input( 'Digite a idade da pessoa: '))

    idade1 += idade
    if sexo == 'F' and idade < 20:
        mulhernova += 1
    elif sexo == 'M' and idade > velho:
        velho = idade
        nomevelho = nome

media = idade1 / qtd
print(35 * '-')
print( ' O nome do homem mais velho:{}'.format(nomevelho))
print(' Total de mulheres com menos de 20 anos:{}'.format(mulhernova))
print(f'A media das idades é: {media:.2f}')
print(8 * '=FIM=')