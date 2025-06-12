import math
angulo = float(input('Digite o Angulo  '))
radianos = math.radians(angulo)
sen = math.sin(radianos)
con = math.cos(radianos)
tan = math.tan(radianos)

print ('Do angulo {} dado o seno, cosseno e Tangente é: {:.4f} , {:.4f} e {:.2f} ' .format(angulo,sen,con,tan))