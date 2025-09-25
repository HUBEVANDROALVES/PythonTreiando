#ler cinco valores e guarda em uma lista, no final mostra o
# maior e menor  valor
maior=menor=valor=0
valor=[]
print("Digite 5 numerosss!!")
print("+="*15)
numeros = int(input(f"Digite o 1ª numero: "))
maior=menor=numeros
valor.append(numeros)
for cont in range (4):
    numeros=int(input(f"Digite o {cont+2}ª numero: "))
    valor.append(numeros)
    if numeros > maior:
        maior = numeros
        pmaior = valor.index(numeros)
    if numeros  < menor:
       pmenor = valor.index((numeros))
print(f"O menor numero esta na {pmenor}ª posição  \n"
      f" e o maior na {pmaior+1}ª posição ")
print(valor)