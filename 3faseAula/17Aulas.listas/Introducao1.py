# LISTA
# sao mutaveis  Dupla imutaveis
lanche=["hambugue","suco","pizza","pudim"]
print(lanche)
lanche[3]="picole"
print(lanche)
lanche.append("cafe")
print(lanche)
print(lanche.index("suco))
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

num = [8,7,2,5,98]
num[0] = 100
num.append(23)#cria mais uma posiçao
print(num)
num.sort()#coloca em orde crescente, se adicionar (reverse=True) fica em decrecentes.sta
num.insert(2,99)# inserir na possicao 2 o numero 99
print(num)
num.pop()# exclui elementos o ultimo elemento
num.pop(0) # exclui o primeiro
num.remove(99)# remove o elemento 99 se houver mais de um, somente o primeiro..
if 99 in num:
    num.remove(99)
    print("Numero 99 removido ")
else:
    print("Nao achei o numero 99 !")
print(num)
print (f"Essa lista tem {len(num)} elementos ")