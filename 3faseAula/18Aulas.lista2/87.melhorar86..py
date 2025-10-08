#melhorar o desafio anterior
# e mostrar soma no caso acima: 45, terceira coluna 18 e
# a soma dos pares 20 e maior valor da segunda linha e 6

#pedir pra digitar 9 numeres e mostra em uma matrix 3x3
# 1.2.3
# 4.5.6.
# 7.8.9.
somapar=somacoluna=maior=0
matriz=[[],[],[]]
print("   Digite uma matriz 3 X 3 ")
print("=-"*15)
for a in range(3):
    for b in range (3):
        numero = int(input(f" Digite um valor para [{a},{b}]: "))
        matriz[a].append(numero)
        if numero % 2 == 0:
            somapar += numero
        if b==2:
            somacoluna += numero
        if a == 1 and numero>maior:
            maior = numero
for linha in matriz:
    for elemento in linha:
        print(f"{elemento:^5}", end="")  # ^5 centraliza em 5
    print()  # quebra de linha

print(somapar)
print(somacoluna)
print(maior)