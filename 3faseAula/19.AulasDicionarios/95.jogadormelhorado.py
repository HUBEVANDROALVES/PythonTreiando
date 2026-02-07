jogador=dict()
partidas=list()
time = list()
while True:
    jogador.clear() # apagar para nao mistura os dados do jogador anterior
    partidas.clear()
    jogador["nome"]=str(input("Digite o nome do jogador: "))
    tot = int(input(f"Quantas partidas {jogador['nome']} jogou?: "))# dentro de aspar duplas usar aspas simples..

    for c in range(0, tot):
        partidas.append(int(input(f"Digite a qtd de gols feito no {c+1}º jogo: ")))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())# cria uma copia indepedente
    while True:
        resp = str(input("Quer continuar? [S/N]")).upper()[0]
        if resp in 'SN': #  a resposta tem que ser sim ou nao..
            break
        print("ERRO ! responda S ou N.")
    if resp == "N":
        break
print('-'*30)
print('cod ',end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k,v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}',end='')
    print()
print('-'*40)
while True:
    busca = int(input('Mostras dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time) :
        print(f'Erro! não existe jogador com codigo {busca} !')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR: {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'     No jogo{i+1} fez {g} gols.')
    print('-' * 40)
print('<< VOLTE SEMPRE >>')