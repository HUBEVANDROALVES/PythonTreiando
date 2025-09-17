tuplaNome=tuplaVogal=tuplaA=()
tuplaE=tuplaI=tuplaO=tuplaU=()
cont=0
while True:
    nome=input("Digite a palavra(ou 'fim' para parar) :  ")
    if nome=="fim":
        break
    tuplaNome +=(nome,)
    vogais = tuple(letra for letra in nome if letra in "aeiou")
    tuplaVogal += (vogais,)
    tuplaA += (nome.count('a'),)
    tuplaE += (nome.count('e'),)
    tuplaI += (nome.count('i'),)
    tuplaO += (nome.count('o'),)
    tuplaU += (nome.count('u'),)


a=0

for i in range(len(tuplaNome)):

    vogais_formatadas = " ".join(tuplaVogal[i]) if tuplaVogal[i] else "nenhuma" #variavel = valor_se_verdadeiro if condição else valor_se_falso
    if "a" in tuplaVogal[i]:
        a += 1
 #   print(f"A palavrar {tuplaNome[i]}  tem as Vogais: {vogais_formatadas}")
    print()
    print(f"Na palavra '{tuplaNome[i]}' o número de \n 'a,e,i,o,u' são respectivamente : {tuplaA[i]} {tuplaE[i]} {tuplaI[i]} {tuplaO[i]} {tuplaU[i]}")