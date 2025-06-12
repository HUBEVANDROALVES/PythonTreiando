from os.path import split

nome = input("Digite o nome da pessoa: ")
palavras = nome.split()

print('O primeiro nome é: {}{}{}'.format('\033[4;31;40m',palavras[0],'\033[m'))
##print("O Ultimo nome é :  {}".format('\033[[palavras[-1]))