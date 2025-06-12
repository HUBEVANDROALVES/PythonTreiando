from random import randint
from time import sleep
itens=('Pedra','Papel','Tesoura')
computador = randint(0,2)
print('''As suas opções:
      [0]   Pedra
      [1]   Papel
      [2]   Tesoura''')
jogador = int(input('Qual é a sua jogada? '))
if jogador<0 or jogador>2:
    print('Jogada invalida')
else:
    print('JO')
    sleep(1)
    print('KE')
    sleep(1)
    print('PON!!!')
    print('=-'*14)
    print('O computador escolheu {}'.format(itens[computador]))
    print('O Jogador escolheu {}'.format(itens[jogador]))
    print('=-'*14)
    if computador==0 and jogador==2 or computador==1 and jogador==2 or computador==2 and jogador==0:
        print('O jogador ganhou !!')
    elif computador==0 and jogador==0 or computador==1 and jogador==1 or computador==2 and jogador==2:
        print('EMPATE')
    ##elif computador==0 and jogador==1 or computador==1 and jogador==0 or computador==2 and jogador==1:
    ##    print('O Computador ganhou')

    else:
        print('Computador ganhou')