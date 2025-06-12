import random


n1 = random.randint(1,3)
cont=0
acertou = False
print(('Acabei de sortea um numero, voce consegue adivinha'))
n2 = int(input('Digite um numero entre 1 e 10 : '))
while not acertou:
     if n1 == n2:
        acertou = True
        cont +=1
     else:
        if n1 > n2:
            print ( 'O numero é maior que {}'.format(n2))
        else:
            print ('O numero é menor que {}'.format(n2))
        n2 =int(input('Digite novamente : '))
print ('Voce acertou na {}º tentativa '.format(cont+1))
