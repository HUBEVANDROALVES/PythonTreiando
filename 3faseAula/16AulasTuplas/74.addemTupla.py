import random
from random import randint
tuplaA=tupla=()
cont=0
numero=0
while cont<=6:
        numero=random.randint(0,100)
        tuplaA+= (numero,)
        cont += 1
print(tuplaA)
tupla=sorted(tuplaA)

print(f"O Menor valor da Tupla é : {(tupla[0])}")
print(f"O Maior Valor da Tupla é :{(tupla[6])}")
print(f'\n')

numeros = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print("Os valores sorteados foram: ", end= ' ' )
for n in numeros:
        print(f'{n}', end=' ,')
print (f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')