# LISTA
# sao mutaveis  Dupla imutaveis
lanche=["hambugue","suco","pizza","pudim"]
print(lanche)
lanche[3]="picole"
print(lanche)
lanche.append("cafe")
print(lanche)
lanche.insert(0,"cachoro quente")
lanche.insert(1,"ovo")
lanche.insert(-3, "ovo")
print(lanche)
del lanche[1] # elimina na possico
print(lanche)
lanche.pop(2) # elimina na posicao
print(lanche)
lanche.remove("picole")# remove pelo nome/conteudo
print(lanche)
print(lanche[0])
if "ovo" in lanche:
    lanche.remove("ovo")
print(lanche)
valores=[8,2,5,4,9,3,0]
print(len(valores))
print(valores)
valores.sort()
print(valores)
valores.sort(reverse=True)
print(valores)

num = [8,7,2,5]
num[0] = 100
num.append(23)#cria mais uma posiçao
num.sort()#coloca em orde crescente, se adicionar (reverse=True) fica em decrecentes.sta
print(num)