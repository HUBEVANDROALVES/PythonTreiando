
numero = int( input('Digite o numero de 0 a 9999: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print('O numero é: {}'.format(numero))
print('A unidade é: {}'.format(u))
print('A Dezena é: {}'.format(d))
print('A centena é: {}'.format(c))
print('A Milhar é:  {}' .format(m))


