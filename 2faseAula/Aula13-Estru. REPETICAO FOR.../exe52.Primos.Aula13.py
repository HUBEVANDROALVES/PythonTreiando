from time import sleep
import math
numero = int(input('Digite um numero: '))

if numero < 2:
    print( f'{numero} nao é um numero primo')
else:
     primo = True
     for i in range(2,int(math.sqrt(numero))+1):
        if numero % i ==0:
                primo = False
                break
     if primo:
            print(f'{numero} é um número primo')
     else:
            print(f'{numero} não é um número primo')
sleep(0.3)

print('FIM')