

saque=int(input("Digite o valor a ser sacado "))
cont1=cont2=cont5=cont10=cont20=cont50=cont100=cont200=0
nota200=nota100=nota50=nota20=nota10=nota5=nota2=nota1=0

'''if saque >=200:
    saque1 = saque
    nota200 = saque1 // 200
    saque=saque1-(nota200*200)'''
if saque >=100:
    saque1 = saque
    nota100 = saque1 // 100
    saque = saque1-(nota100*100)
if saque >= 50:
    saque1 = saque
    nota50 = saque1 // 50
    saque=saque1-(nota50*50)
'''if saque >= 20:
    saque1=saque
    nota20 = saque1 // 20
    saque=saque1-(nota20*20)'''
if saque >= 10:
    saque1=saque
    nota10 = saque1 // 10
    saque=saque1-(nota10*10)
if saque >= 5:
    saque1=saque
    nota5 = saque1 // 5
    saque = saque1-(nota5*5)
    nota1 = saque
print(f"{nota200},{nota100},{nota50},{nota20},{nota10},{nota5},{nota1}")


'''u = numero // 1 % 10®
d = numero // 10 % 10
c = numero // 100 % 10'''