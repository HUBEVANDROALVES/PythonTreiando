

numero2=("Zero","Um","Dois","Tres","Quatro","Cinco","seis","Sete","Oito","Nove",
         "Dez","Onze","Doze","Treze","Quatorze","Quinze","Dezeseis","Dezessete","Dezoito","Dessenove","Vinte")
while True:
    numero=int(input("Digite um numero entre 0 e 20: "))
    if  0 <= numero <= 20:
        break
    print ("Tente novamente ", end=" " )


print(f"Voce digitou o numero {numero2[numero]}")