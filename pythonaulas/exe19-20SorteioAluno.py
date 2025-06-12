import math
import random

aluno1=(input( 'Digite o nome do primeiro aluno '))
aluno2=(input( 'Digite o nome do segundo aluno '))
aluno3=(input( 'Digite o nome do terceiro aluno '))
aluno4=(input( 'Digite o nome do quarto aluno '))

listalunos = [aluno1,aluno2,aluno3,aluno4]
sorteado = random.choice(listalunos)# RETIRANDO UM ALUNO
random.shuffle(listalunos)# embarralha a lista

print('Quem vai apagar o quadro é {} '  .format(sorteado))
print (listalunos)
print ('A orde de apresentacao é  ')
for i, aluno in enumerate(listalunos,1) :
    print(f'{i}.{aluno}')
#  {i} → Exibe o número da ordem de apresentação.
#  {aluno} → Exibe o nome do aluno.
#O f antes das aspas permite usar variáveis diretamente dentro da string.
