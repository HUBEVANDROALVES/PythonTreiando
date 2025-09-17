

cont1=0
num=0
tot=0
num = int(input(f'Digite o {cont1+1}º numero[999 para parar]: '))
while num != 999:
    cont1 += 1
    tot   += num
    num = int(input(f'Digite o {cont1}º numero[999 para parar]: '))

print(f'Voce digitou {cont1} numeros e o total foi {tot}')
print ('Fim')