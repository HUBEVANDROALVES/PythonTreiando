import math

numero = int(input('Digite um numero '))
print("o numero é:" )
antecessor = numero-1
sucessor = numero+1

print('O NUMERO É {}, \n O ANTECESSOR É:{}, \n E O SUCESSOR É:{}' .format(numero, antecessor, sucessor))

numero2 = int(input('Digite outro numero:  '))
dobro = numero2 * 2
triplo = numero2 * 3
raiz = math.sqrt(numero2)
print('O numero é: {}, \n O DOBRO É {} , \n O TRIPLO É: {} , \n A raiz quadrada  é: {:2f}'  .format(numero2, dobro, triplo, raiz))

# DESAFIO 7
nota1 = int(input('Digite a primeira nota: '))
nota2 = int(input('Digite a segunda nota:  '))
media=  (nota1+nota2)/2
print ('A media das primeira nota  {:.1f} \n e da segunda nota {} \n é {} ' .format(nota1,nota2,media))
