import math

idade=int(input('Digite a sua idade: '))
tempo=0

if idade == 18:
    print ('Ja esta na hora de voce se alistar')
elif idade>18:
    tempo=idade-18
    print ('Voce deveria ter se alistado há \n {} Anos'.format(tempo))
else:
    tempo=18-idade
    print ('Ainda faltam {} Anos pra voce se alistar'.format(tempo))