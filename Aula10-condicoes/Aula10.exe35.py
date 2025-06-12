reta1=int(input('Digite o tamanho da 1º reta: '))
reta2=int(input('Digite o tamanho da 2º reta: '))
reta3=int(input('digite o tamanho da 3º reta: '))

if reta1<(reta3+reta2) and reta2<(reta3+reta1) and reta3<(reta1+reta2):
    print('As retas  fazem um triangulo  ')
else:
    print('As retas nao  podem fazer um triangulo ')