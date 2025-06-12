import math
qtd = int(input('Quantas pessoas vao ser pesadas: '))
mais=0
menos=0
nmais=0
nmenos=0
for i in range(0,qtd,1):
    peso = int(input('Qual o peso  da {}º pessoa:  '.format(i+1)))
    if i == 0:
        mais=peso
        menos=peso
        nmais=i+1
        nmenos=i+1
    else:

        if peso  > mais:
            mais = peso
            nmais = i+1
        elif peso <= menos:
            menos = peso
            nmenos = i+1

print(mais,menos,nmais,nmenos)