import math
altura=float(input('Digite a sua altura: '))
peso=float(input('Digite o seu peso: '))
imc=peso/(altura*altura)
print ('O seu IMC é {:.2f}'.format(imc))
if imc<18.5:
    print ('Você esta abaixo do peso!')
elif 18.5<imc<25:
    print('\033[33m')
    print('Você esta com o peso ideal!')
elif 25<imc<30:
    print('\033[31m')
    print ('Voce esta acima do peso!')
elif 30<imc<40:
    print ('Você esta obeso !!')
else:
    print('Você esta com Obesidade morbida!!')
