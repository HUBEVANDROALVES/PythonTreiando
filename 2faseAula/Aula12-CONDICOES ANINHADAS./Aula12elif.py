from traceback import print_exc

nome = input('qual o seu nome:  ')
nome1 = nome.lower()

if nome1 == 'hubevandro':
    print('Que nome bonito')
elif nome1=='joao' or nome1=='carla' or nome1=='pedro':
    print('Seu nome e bem popular')
elif nome1=='maria' or nome1=='jessica':
    print('Belo nome feminino')
else:
    print('Seu nome e bem normal.')
print('Bom dia {}'.format(nome))
