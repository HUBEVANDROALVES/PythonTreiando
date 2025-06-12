import random
num = random.randint(1,5)
num1=int(input("Escolha um numero de 1 a 5:  "))
print('O numero sorteado foi: {} '.format(num))

if num==num1:
    print('\033[4;32m''voce acertou''\033[m')
else:
    print('\033[0;31;40m''Voce errou''\033[m')