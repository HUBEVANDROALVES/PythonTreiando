import math
nota1=float(input('Digite a primeira nota: '))
nota2=float(input('Digite a segunda nota: '))
media=(nota1+nota2)/2

if media<5:
    print('Voce foi Reprovado')
elif 5<media<7:
    print("Voce esta na recuperacao ")
else:
    print('Voce foi aprovado')