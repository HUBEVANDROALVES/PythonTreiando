from time import sleep
primeiro=int(input('Digite o primeiro termo: '))
razao=int(input('Digite a razao: '))
cont=1
pa=primeiro
while cont != 11:
    print(primeiro,'-> ', end='')
    primeiro += razao
    sleep(.3)
    cont+=1
print('fim')