
import time
valores = []  # ou valores = list()
#valores.append(5)
#valores.append(9)
#valores.append(4)
for cont in range(0, 5):  # em cima estamos colocando um por um, abaixo atraves do for
    valores.append(int(input( "Digite um valor !")))
   #time.sleep(1)

for c,v in enumerate(valores):  # enumeras os valores com duas variaveir
    print(f"Na posicao {c+1} encontrei o valor {v} !")
    time.sleep(0.5)
print("Chequei ao final da lista ")

a=[2,3,4,7]
#b=a # faz uma ligacao entre A e B.. ex..
b = a[:]  # AGORA ELE CRIAR UMA COPIA SE EU FIZER B[2]=8 SOMENTE EM B VAI MUDAR
b[2]=8 # o numero muda nas duas listas

print(a)
print(b)