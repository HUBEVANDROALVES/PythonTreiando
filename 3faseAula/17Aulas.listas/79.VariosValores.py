##Digitar vario valores e excluir os repetidos

numero=0
lista=[]
i=1
while True:
    numero = int(input(f"Digite o {i}º número: "))
    i += 1
    if numero in lista:
        print(f"O número {numero} já foi digitado, tente outro !")
    else:
        lista.append(numero)
    fim=input("Deseja termina ? digite S/N :" ).upper()
    if fim=="S":
        break
print("acabou ")
print(sorted(lista))