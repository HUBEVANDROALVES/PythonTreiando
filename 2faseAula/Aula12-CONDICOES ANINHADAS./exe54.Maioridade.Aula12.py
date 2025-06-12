import math
from datetime import datetime
n = int(input('Quantas datas vao ser digitadas:  '))
demaior=0
demenor=0
for i in range(n):
    datastr = input(f'Digite a data nascimento da  {i+1}º pessoa, formato (dd/mm/aaaa):')
    data = datetime.strptime(datastr, "%d/%m/%Y").date()
    limite = datetime.strptime("18/05/2007", "%d/%m/%Y").date()
    if data <= limite:
        demaior=demaior+1
    else:
        demenor=demenor+1

print(demaior)
print(demenor)
print(n)

