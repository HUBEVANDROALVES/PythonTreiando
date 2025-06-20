from time import sleep
print('            Gerador de PA        ')
print('*'*40)

numero=int(input('Digite primeiro termo :  '))
razao=int(input('Digite a razão: '))
cont=1
qdt=1
mais=10
total=0

while mais != 0:
    total=total+mais
    while cont<=total:
        print(f'{numero} ->', end='' )
        numero+=razao
        cont+=1
    print(' Pausa')
    mais=int(input("quanto termos mais vôce quer mostrar ? "))
print(f' Progressao finalizada com {total} termos')
print('FIM')



