import math
anonasc=int(input('Digite o ano de nascimento da criança: '))


if anonasc>=2016:
    print('A categoria é Mirim ')
elif anonasc>=2011:
    print('A Categoria é Infantil ')
elif anonasc>=2006:
    print('A categoria é Junior')
elif anonasc>=2005:
    print('A categoria é Senior')
else:
    print ('A categoria e Master ')