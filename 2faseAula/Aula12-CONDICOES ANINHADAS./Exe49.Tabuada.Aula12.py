import math
from time import sleep

tabuada = int(input('Digite um numero: '))
total=0

print('=' * 18)
for i in range(10,0,-1):
    total = tabuada * i
    print('++++{} X {} = {}'.format(tabuada,i,total))
    sleep(1)
print('=' * 18)