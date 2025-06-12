import math
#from collections.abc import range_iterator
from time import sleep

frase=input('Digite a frase: ').replace(" ","")
#print(len(frase))
#print((frase.split()))
#print(frase)
#contador=len(frase)
#print(contador)
fraselimpa=frase.replace(' ','').strip()
frasepalidromo=fraselimpa[::-1]
print(frase)
print(frasepalidromo)
if frase == frasepalidromo:
    print('essa frase é um palidromo')
else:
    print(('Essa frase não e um palimdromo'))

frase2 = input( 'Digite outra frase: ')

print(frase2)
palavras2=frase2.split()
juntas=''.join(palavras2)
print(juntas)
inverso=''
for i in range(len(juntas)-1,-1,-1):  # ler a palavra partindo da ultima letra.. vai ate o -1,
    #print(juntas[i])
    inverso += juntas[i]

if inverso == juntas:
        print('A palavra é um palindromo')
else:
        print('A palavra não é um palindromo')
#print(inverso)


