ano = int(input('Digite o ano '))
resto = ano % 4

if resto==0:
    print('\033[1;32m''Esse ano e Bissexto ')
else:
    print('\033[1;31;43m''Esse ano não e Bissexto''\033[44m')
