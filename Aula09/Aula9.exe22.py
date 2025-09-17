from os.path import split

nome = input('Digite o nome completo: ')
nome1=input("Par ou Impar (P/I)  ? ").strip().upper()
print(nome.upper())
print(nome.lower())
print(nome1.upper())
print(nome1.lower())
total=len(nome)-(nome.count(' '))
print('seu nome tem {} letras' .format(total))
print(nome.split())
dividindo = nome.split()[0]
print('O Primeiro nome "{}" tem {} letras'.format(dividindo, len(dividindo)))