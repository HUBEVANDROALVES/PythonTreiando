alt = int(input(' Qual a altura da parede em metros ?   '))
lar = int(input(' Qual a largura da parede em metros ?  '))
area = alt*lar
litro = area/2

print ("A Area da sua parede é {}m e voce vai precisar {} litros de tintas pra pintar a parede" .format(area,litro))