import math

preco=float(input('Qual o valor do produto: '))
forma=input('Qual a forma de pagamento\n A) A Vista Dinheiro \n B) Cartão à vista'
                  ' \n C) Cartão 2 Vezes \n D) Cartão 3 Vezes \n')
novovalor=float(0)

if forma=='a':
    novovalor=preco*0.90
    print ('O valor a vista tem desconto de 10% \n novo valor: {}'.format(novovalor) )
elif forma=='b':
    novovalor=preco*0.95
    print('O Valor no Cartao a vista tem desconto de 5% \n novo valor {}'.format(novovalor))
elif forma=='c':
    novovalor=preco
    print('O Valor no cartao em 2 vezes nao tem acrecimo \n o valor é {}'.format(novovalor))
elif forma=='d':
    novovalor=preco*1.20
    print('O valor no cartao em 3 vezes ou mais tem 20% de acrescimo \n o novo valor é {} '.format(novovalor))
else:
    print('opcao errada digite A,B,C OU D')