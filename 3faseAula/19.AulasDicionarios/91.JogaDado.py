## cria um programa que onde 4 jogadores joguem um dado
## e tenha resultados aleatorios.
##Guarde esses resultados em um dicionario. No final
## coloque esse dicionario em ordem mostrando o jogador com a maior
## VAlor

from random import randint
from time import  sleep
from operator import itemgetter
jogador={}

for i in range(1,5):
    dado = randint(1,6)
    jogador[f"Jogador {i}"]=dado
print ("Resultados: ")
for k, v in jogador.items():#
    print(f"{k}:{v}")

ranking = sorted(jogador.items(), key=itemgetter(0), reverse=True)

print("\nRanking final:")
for pos, (k, v) in enumerate(ranking, start=1): #
    print(f"{pos}º lugar: {k} com {v}")         #

