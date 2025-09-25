
# pedir 5 numeros e ordenar sem usar o SORT()

numero=maior=menor=0
lista=[]
cont=i=j=n=0
while len(lista) < 5:
    numero=int(input("Digite um numero: "))
    lista.append(numero)
  #  if len(lista) == 5:
  #      break
    n=len(lista)
    for i in range(n):
        for j in range(0,n-i-1):
            if lista[j] > lista[j+1]:
                lista[j],lista[j+1] = lista[j+1], lista[j]

print("acabou ")
print(lista)