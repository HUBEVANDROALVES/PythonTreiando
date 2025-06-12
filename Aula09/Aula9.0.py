from xml.sax.handler import property_encoding

frase = 'curso em video python videos'
frase2 = '   Aprenda python   '

###   FATIAMENTO
print (frase[9])
print (frase[9:13])   # o inicio 9 mostra o 13 nao mostra
print (frase[9:21:2])  # inicia no 9 ate o 20 de dois em dois.
print (frase [9:21])
print (frase[:5])
print (frase[9:])
print (frase[9::3])  # comeca no nove vai ate o final, comeca no primeiro vai ate o terceiro
len(frase)  # mede o tamanho da frase , quantos caracteres
print(len(frase))# o tamanho da frase
print(frase.count('o',0,20))# conta quantas letra o tem da posicao 0 a 13.
print(frase.find('deo'))# mostra a posicao 'deo'  na frase
print(frase.find('mar'))
print(frase.replace('video','filme')) # substitui a palavras OBS: VIDEO substitui VIDEOS tambwm o inverso nao
print(frase.upper())# transforme maiusculos
print(frase.lower())# transformar em minusculos
print(frase.capitalize()) # a primeira palavra inicia em maiusculo
print(frase.title())
print(frase2.strip()) # retira os espacos inuteis. RSPRIT na diereita e LSPRIT na esquerda
print(frase2.rstrip())
print(frase2.lstrip())
    ###################  DIVISÃO    ###########
print(frase.split())  ## divide a frase
print('-'.join(frase.split(' ')))  #### coloca o simbolo escolhido entre as palavras no caso foi ''por '-


