reta1=int(input('Digite o tamanho da 1º reta: '))
reta2=int(input('Digite o tamanho da 2º reta: '))
reta3=int(input('digite o tamanho da 3º reta: '))

if reta1<(reta3+reta2) and reta2<(reta3+reta1) and reta3<(reta1+reta2):
    print('As retas  fazem um triangulo  ')
    if reta1==reta2==reta3:
        print('É é triângulo Equilátero')
    elif reta1==reta2 or reta1==reta3 or reta3==reta2:
        print( 'E é um triângulo Isósceles')
    else:
        print('E é  um triâgulo escaleno ')
else:
    print ('As retas não fazem um triangulo')