#criar um programa pra criar uma lista
# nome de jogador, quantidade de partidas e gols feitos nos jogos.
#mostra no final nome do jogador e total de gols
jogador=dict()
jogador["nome"]=str(input("Digite o nome do jogador: "))
jogador["qtdjogos"]=int(input(f"Quantas partidas {jogador["nome"]} jogou?: "))
jogador["gols"] = []
for i in range(0,jogador["qtdjogos"]):
    gol = int(input(f"Digite a qtd de gols feito no {i+1}º jogo: "))
    jogador['gols'].append(gol) # guarda os gols
print("=-"*35)
print(jogador)
print("=-"*35)
for k,v in jogador.items(): # mostra a lista jogador...
    print(f"O Campo {k} tem valor {v}")
print('-='*35)
print(f"O Jogador {jogador["nome"]} jogou {jogador["qtdjogos"]} partidas.")
for i, gol in enumerate(jogador["gols"], start=1):
    print(f"==> Na {i}ª partida fez {gol} gol(s)")  ## mostra a lista de gosl feito por partida

