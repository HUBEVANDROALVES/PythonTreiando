from selectors import SelectSelector
from sys import flags

tempo = int(input('Digite a idade do carro:  '))
print('Carro novo'
      if tempo<=3
      else 'Carro Velho')
print ('Fim do programa')


n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda  nota: '))
media = (n1+n2) / 2
print('A sua media é {}' .format(media))
if media >= 7:        ## nao esquecer os dois pontos
      print('voce passou')
else:
      print('Reprovado')

print('Voce passou ' if media >= 7 else 'reprovado')
