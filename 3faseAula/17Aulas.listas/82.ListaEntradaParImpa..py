# lista de entrada numeros aleatorio e saida lista de par ou impar. 

lista=[]
listapar=[]
listaimpa=[]
numero=0
while True:
    numero=int(input("Digite o Numero: "))
    lista.append(numero)
    if numero % 2 == 0:
        listapar.append(numero)
    else:
        listaimpa.append(numero)
    fim=input("Deseja terminar digite S: ").upper()
    if fim == "S":
        break
print(lista)
print(listapar)
print(listaimpa)
