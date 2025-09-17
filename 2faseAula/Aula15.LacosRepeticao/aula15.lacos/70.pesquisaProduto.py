
print("-"*25)
print("   LOJA SUPER BARATÃO")
print("-"*25)
nome=NomeMaior=NomeMenor=""
preco=Mais1000=MaisBarato=Total=menor=0
cont1=cont2=0
while True:
    nome=input("Nome do Produto: ")
    preco=int(input("Qual o Preco R$: "))
    Total += preco
    cont1 += 1
    print(" ")
    if cont1 == 1:
        MaisBarato=preco

    if preco > 1000:
        cont2 += 1
    if   preco < MaisBarato:
        NomeMenor=nome
        MaisBarato=preco
    encerra = input("Deseja continuar S/N").upper().strip()[0]
    if encerra == "N":
        break
print("-"*6,"FIM DO PROGRAMA","-"*6)
print(f"O Total da compra foi R${Total:.2f} \n "
      f"Temos {cont2} produtos  custando mais de R$ 1000.00 \n"
      f" O Produto mais barato foi o ({NomeMenor}) que custa R$ {MaisBarato:.2f}")

