import math

num=int(input('Digite um numero: '))
tipo=str(input('Digite a,b ou c para: \n A)Binario \n B)Octal \n C)Hexadecimal'))
if tipo=='a':
    print('O numero que escolhido na base Binario é {}'.format(bin(num)[2:]))
elif tipo=='b':
    print( 'O numero escolhido na base Octal é {}' .format(oct(num)[2:]))
elif tipo=='c':
    print( 'O numero escolhodo na base hexadecimal é {} '.format(hex(num)[2:]))
