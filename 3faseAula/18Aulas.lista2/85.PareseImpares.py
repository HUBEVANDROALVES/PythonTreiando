#pedir sete valores e separar pares e impares.

par=list()
impar=list()
print("Digite 7 numeros: ")
print("=-"*12)
for i in range(1,8,1):
    numeros=int(input(f"Digite o {i}ª numero : "))
    if numeros % 2 == 0:
        par.append(numeros)
    else:
        impar.append((numeros))



print ("fim ")
print(f"Os numeros pares digitador foram \n {par}")
print(f"Os numeros impares digitados foram\n {impar}")