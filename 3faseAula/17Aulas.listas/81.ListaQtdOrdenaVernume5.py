#pedir para digitar valores em uma lista, com a indicacao para parar,
#apos mostra a quantidade de elementos, em orde decrecente e se o numero 5 foi digirado
from operator import truediv

lista=[]
listaord=[]
cont=0
cinco=False
while True:
    numero=int(input("Digite um numero: "))
    lista.append(numero)
    cont += 1
    if numero == 5:
        cinco = True
    sair = input("Deseja terminar  Sim ou Nao: ").upper()

    if sair == "S":
        break
listaord = sorted(lista, reverse=True)
print("-="*30)
print(f"Você digitou {cont} elementos \nOs Valores em ordem decrescente são: {listaord}")
if cinco:
    print("O número 5 faz SIM parte de lista")
else:
    print("O número 5 NÃO faz parte de lista ")

