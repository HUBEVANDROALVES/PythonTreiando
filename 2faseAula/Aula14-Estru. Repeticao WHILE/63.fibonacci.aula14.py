
qtd=int(input('Digite a quantidade de termos a parti de 5: '))
n1=0
n2=1
print(f'A Sequencia de fibonacci com {qtd} termos ')
print(f'{n1} ->{n2}', end='')
cont=3
while cont <= qtd:
    n3=n1+n2
    print(f'-> {n3}',end='')
    n1=n2
    n2=n3
    cont += 1
print('->fim')