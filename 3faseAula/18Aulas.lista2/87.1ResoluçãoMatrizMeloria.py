matriz = [[0,0,0],[0,0,0],[0,0,0]]
somapar=stercoluna=maiorL1=0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l},{c}]: '))
print('-='*30)
for l in range(0,3):
    for c in range(0,3):
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
        if c == 2:
            stercoluna += matriz[l][c]
        print(f"[{matriz[l][c]:^5}]",end="")
    print()
print(f" A soma dos valores da terceira coluna é: {stercoluna} ")
print(f" A soma dos valores par é : {somapar}")
for c in range(0,3):
    if c == 0:
        maiorL1  = matriz[1][c]
    elif matriz[1][c] > maiorL1 :
        maiorL1 = matriz[1][c]
print(f" O Maior valor da segunda linha  é :{maiorL1}")