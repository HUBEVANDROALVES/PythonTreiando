frase=input(('Digite ai  '))
frase1=frase.lower().strip()# torna tudo minusculo e elimina os espaco em branco

print('a letra A aparece: {} vezes' .format(frase1.count('a')))
print ('a primeira vez na posicao: {}'.format(frase1.find('a')))
print ('e pela ultima vez na posicao: {}'.format(frase1.rfind('a')))