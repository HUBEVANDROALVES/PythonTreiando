# entrar com uma expressao e verificar se e valida ou nao
from time import sleep
# (9*(45/5)(8/(2+2)*9)(7+6))
listaexp=[]
from time import sleep
cont=0
aspaAbre=0
aspaFecha=0
expressao=input("Digite a expressão: ")
listaexp = list(expressao)

while len(listaexp) > cont:
    if  listaexp[cont] == "(":
        aspaAbre += 1
    if  listaexp[cont] == ")":
        aspaFecha += 1
    cont += 1


if aspaFecha==aspaAbre:
    print ("Expressão válida!")
else:
    print ("Expressão Inválida!")
print("fim")

