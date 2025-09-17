serieA=( "Flamengo", "Cruzeiro", "Palmeiras", "Bahia", "Botafogo",\
    "Mirassol", "São Paulo", "Bragantino", "Fluminense", "Internacional",\
    "Ceará", "Corinthians", "Grêmio", "Atlético-MG", "Vasco da Gama",\
    "Santos", "Vitória", "Juventude", "Fortaleza", "Sport")

print("-="*33)
print(f"        Lista dos times Brasileiro Serie A: ")
print("-="*33)
for i,n in enumerate(serieA,1):
    print(f"{n:>3}", end=" , ")
    if i % 5 ==0:
        print()
print("-="*33)
print("Os 5 primeiros colocados são ")
print(serieA[:5])
print("-="*33)
print("Os 4 Ultimos lococados sao: ")
print(serieA[-4:])
print("-="*33)
##print(sorted(serieA))  ordem alfabetida
for i,n in enumerate(sorted(serieA),1): #ENUMERA
    print(f"{n:>3}", end=" , ")         #
    if i % 5 ==0:
        print()
print("-="*33)
posicao=serieA.index("Sport")
print(f"O SPORT esta na {posicao + 1}ª Colocação.")
print(f"O Vitoria esta na {serieA.index("Vitória")+1}ª posição")