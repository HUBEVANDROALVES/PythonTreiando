
import random
cont=0
parImpa=" "
print("=-"*15)
print("Vamor Jogar Par ou Impar ?")
print("=-"*15)

while True:
    computador = random.randint(1, 10)
    print(f" Numero escolhido {computador}")
    jogador=int(input("Diga um valor: "))
    soma=computador+jogador

    parImpa=" "
    while parImpa not in "PI":
        parImpa=input("Par ou Impar (P/I)  ? ").strip().upper()[0]

    if soma % 2 == 0 and  parImpa == "P" or soma % 2 == 1 and parImpa == "I":
            print("=-" * 20)
            print(f"Você jogou {computador} e o computador {jogador} Soma: {soma} ")
            print("=-"*20)
            print("Você Ganhou")
            print("Vamos Jogar novamente...")
            cont +=1
            print("=-" * 20)

    else:
        print (f"Você perdeu ! Jogou {jogador} e o computador {computador}. Soma: {soma}")
        break

print("-"*20)
print(f"Game Over!! Você venceu {cont} Vezes")
print("-"*20)



