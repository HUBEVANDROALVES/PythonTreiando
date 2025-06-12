import math
from time import sleep
numero1=int(input('Digite o primeiro termo : '))
razao=int(input('Digite a Razao da PA: '))
decimo=numero1+9*razao
for i in range(numero1,decimo,razao):
    numero1=numero1+razao
    print( i, end= '  \u2192  ')
    sleep(0.5)
print(numero1)



