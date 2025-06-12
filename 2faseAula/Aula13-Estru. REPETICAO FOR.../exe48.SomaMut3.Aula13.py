from time import sleep
import math
n=int(input('Digite numero: '))
resto = n % 3
soma = 0
cont=0

if resto == 1:
    n = n-1
elif resto == 2:
    n = n-2
for  i in  range(n, 0, -3):
    if i % 2 == 1:
        soma = soma + i
    print (soma)

print ('A soma dos numeros impares e mutiplo de 3 \nentre 1 e {} é \n     {}'.format(n,soma))
print('Fim')

numero2 = int(input('DIGITE UM NUMERO '))
soma2 = 0

for i in range(numero2, 0, -1):
    if numero2 % 2 == 1 and numero2 % 3 == 0:
        soma2 = soma2 + numero2

print (soma)
