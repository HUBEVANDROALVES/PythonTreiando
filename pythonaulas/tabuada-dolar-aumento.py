numero = int(input('Digite um numero inteiro: '))
print('Abaixo a tabuada do numero digitado \n {} X 1 =  \n {} X 2 = ' .format(numero,numero))

num = int(input('Digite o numero da tabuada '))
print ('-' * 12)
print ('{} X {:2} = {}' .format(num, 1, num*1))
print ('{} X {:2} = {}' .format(num, 2, num*2))
print ('{} X {:2} = {}' .format(num, 3, num*3))
print ('{} X {:2} = {}' .format(num, 4, num*4))
print ('{} X {:2} = {}' .format(num, 5, num*5))
print ('{} X {:2} = {}' .format(num, 6, num*6))
print ('{} X {:2} = {}' .format(num, 7, num*7))
print ('{} X {:2} = {}' .format(num, 8, num*8))
print ('{} X {:2} = {}' .format(num, 9, num*9))
print ('{} X {:2} = {}' .format(num,10,num*10))
print('_' * 12)






real = int(input('Quanto voce tem na carteira ?  '))
cotacao = int(input ('Qual a cotação do dolar hoje ?  '))
dolar = real/cotacao
print('com R$ {:.2f}  voce compra  D$ {:.2f}  hoje' .format(real, dolar))


preco = float(input ('Digite o preco do produto:  '))
aumento = preco * 0.95
print('O valor do produto com o desconto  é {}' .format(aumento))

salario = int(input("Digite o valor do seu salario:  "))
AumSala = salario * 1.15
print('O seu salario com aumento é R$ {:,.2f}' .format(AumSala))








