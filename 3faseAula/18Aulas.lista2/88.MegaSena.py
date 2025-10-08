#penguntar a quantidade de jogos a ser feitos, e gerar
# aposta de 6 digitos..
import random
sena1=[]

qtd=0
qtd = int(input("qual a quantidade de jogos a serem feitos? "))
for i in range(qtd):
    jogo = []
    while len(jogo)<6: # garante que tera 6 numeros.
        sena=random.randint(1,60)
        if sena not in jogo: # evita a repeticao
            jogo.append(sena)
    jogo.sort()# ordena o jogo
    sena1.append(jogo)
print("\nJogos gerados:")
for idx, jogo in enumerate(sena1, start=1):
    print(f"Jogo {idx}: {jogo}")