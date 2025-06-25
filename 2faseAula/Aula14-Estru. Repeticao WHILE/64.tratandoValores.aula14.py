
cont=0
numeros=0
total=0
while numeros!=999:
    numeros=int(input(f'Digite o {cont+1}º número[999 para parar]: ' ))
    cont+=1
    if numeros != 999:
        total+=numeros
print(f'Vôce digitou {cont-1} números e o total foi {total}')

cont1=0
num=0
tot=0
num=int(input(f'Digite o {cont1+1}º numero[999 para parar]'))
while num != 999:
    cont1+=1
    tot+=num
    num = int(input(f'Digite o {cont1}º numero[999 para parar] '))
print(f'Voce digitou {cont1} numeros e o total foi {tot}')
print ('Fim')