from os.path import split

nome = input('Digite o nome completo: ')
print(nome.upper())
print(nome.lower())
total=len(nome)-(nome.count(' '))
print('seu nome tem {} letras' .format(total))
print(nome.split())
dividindo = nome.split()[0]
print('O Primeiro nome "{}" tem {} letras'.format(dividindo, len(dividindo)))