##  CODIGO ANSI,
##  \033[m   entre o

###### STYLE   TEXT    BACK
print('\033[0;31;40m  ola mundo!\033[m')
print('\033[0;32;40m  ola mundo!\033[m')
print('\033[1;34;42m  ola mundo!\033[m')
print('\033[1;33;43m  ola mundo')
print('\033[4;34;44m  ola mundo')
print('\033[4;35;45m  ola mundo')
print('\033[7;36;46m  ola mundo')
print('\033[7;36;47m  ola mundo!\033[m')

nome1 = 'Guanabara'
nome2 = 'Hubevandro'
cores = {'limpa':'\033[m',
      'azul':'\033[34m',
     'amarela':'\033[33m',
      'pretoebranco':'\033[7;30m'}

print('Olá! Muito praze em te conhecer, {}{}{}!!!'.format('\033[4;34m', nome1, '\033[m'))
print('Olá! Muito praze em te conhecer, {}{}{}!!!'.format(cores['amarela'], nome2, cores['azul']))