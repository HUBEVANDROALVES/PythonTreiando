n1 = int(input('Digite um valor:   '))
n2 = int(input('Digite um segundo valor:  '))
soma = n1+n2
multi = n1*n2
div  = n1/n2
divint = n1//n2
poten = n1**n2
print ('A soma é: {},\n a multiplicação é {} e a divisão é: {:.3f} ' .format(soma,multi,div), end='>>>')
print ('A Divisão inteira é {} ,\n e a potencia é {} '.format(divint, poten))
