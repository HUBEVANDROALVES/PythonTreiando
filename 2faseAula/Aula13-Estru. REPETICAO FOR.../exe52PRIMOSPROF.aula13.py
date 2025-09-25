num = int(input( 'Digite um numero: '))
cont=0

for i in range(1 ,num+1):
    if num % i == 0:
 #       print('\33[33m', end='')
        cont += 1
    else:
        print('\33[31m' , end= '')
  #  print('{}'.format(i),end=',')
if cont==2:
    print('\n \033  O numero {} é primo'.format(num),end=' ')
else:
    print('\n \034 O NUMERO NAO E PRIMO')