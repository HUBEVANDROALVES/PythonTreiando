
cont=media=soma=maior=menor=0
sair=''
while sair!='N':
    num = int(input('Digite um numero '))
    cont += 1
    soma += num
    if cont==1:
        maior=menor=num
    else:
        if num > maior:
            maior=num
        if num < menor:
            menor=num
    sair = str(input('Deseja continuar S/N : ').strip().upper())

    media=soma/cont
print(f'voce digitou {cont} numeros e a media deles é {media:.2f} ')
print(f'O menor numero é {menor} e o maior  é {maior}')