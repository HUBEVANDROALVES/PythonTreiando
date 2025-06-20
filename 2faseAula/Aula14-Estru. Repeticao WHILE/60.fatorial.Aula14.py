from math import factorial
numero=int(input("Digite o número para o fatorial:  "))
fatoria=factorial(numero)
print("O Fatoria de {} é {}".format(numero,fatoria))

n=int(input("Digite o numero para o fatorial: "))
c=n
f=1
print('Calculando o {}! = '.format(n), end='')
while c > 0:
        print('{}' .format(c), end='')
        print(' x ' if c > 1 else ' = ', end=' ')
        f = f * c
        c -= 1
print (f)

n2=int(input('Digite o numero que voce quer fatorar:  '))
