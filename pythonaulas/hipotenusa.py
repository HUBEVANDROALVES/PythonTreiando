import math

Oposto = int(input( ' digite o valo do cateto oposto: '))
Adjacente = int(input('Digite o valo do cateto Adjacente:  '))
Hipo = math.hypot(Oposto,Adjacente)

print('o valor da hipotenusa é: {} ' .format(Hipo))
