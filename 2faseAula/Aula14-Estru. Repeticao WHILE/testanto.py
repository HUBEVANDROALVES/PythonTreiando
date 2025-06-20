numero = int(input("Digite o numero para fatorar: "))
fatorial=1
for  i in range(numero,0,-1):
    fatorial *= i
print('O Fatorial de {} é {}'.format(numero,fatorial))
print(f'O Fatorial de {numero}  é {fatorial}')