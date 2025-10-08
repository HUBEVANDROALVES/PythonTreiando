import math
soma = 0
for i in range(1, 7, 2):
    numero = int(input('Digite o {}º numero: '.format(i)))
    if numero % 2 == 0:
        soma +=  numero
print (soma)


