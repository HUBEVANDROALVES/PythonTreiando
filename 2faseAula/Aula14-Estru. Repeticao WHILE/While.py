from time import sleep
'''for c in range (1,10):
    print(c)
    sleep(.3)
print ('FIM ')'''

c=1
while c < 10:
    print(c)
    c=c+1
    sleep(.3)
print ('fim')
##  QUANDO NAO SE SABE O LIMITE

n=1
r='S'
par=0
impar=0
while  n != 0:  # enquanto o numero for diferente de 0
    n = int(input('Digite um valor: '))
  #  r=str(input(('Deseja para S ou N ' )).upper())
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1

print('fim', par, impar)
