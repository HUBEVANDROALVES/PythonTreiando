
sexo = str(input("informe seu sexo M/F: ").strip().upper()[0])
#while sexo != "M" and sexo != 'F':
while sexo not in ( 'M', 'F' ):
    print ('Valor digitado incorreto é M ou F')
    print(sexo)
    sexo =input ( 'Digite corretamete: ').strip().upper()[0]
print ("ok vc digitou correto")