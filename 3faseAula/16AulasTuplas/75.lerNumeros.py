
numero=0
cont=par=0
tuplaA=()
tuplaB=()
tuplaC=()
tuplaD=()
while True:
    numero=int(input(f"Digite o {cont+1}ª numero: "))
    if numero % 2 == 0:
        par += 1
        tuplaC=(numero,)

    tuplaA+=(numero,)

    cont +=1
    if cont == 4:
        break
print(f"Os numeros pares digitados foram {(tuplaC)}")
print( f"O numero 9 foi digitado {(tuplaA.count(9))} vezes." )
print( f"O numero 3 aparece pela primeira vez na {(tuplaA.index(3)+1)} posição.")