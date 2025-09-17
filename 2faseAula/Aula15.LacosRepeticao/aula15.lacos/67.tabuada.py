from time import sleep
valor=cont=0
while True:
    valor = int(input("Quer ver a tabuada de qual valor: "))
    print("-"*13)
    if valor<0:
        break
    cont=0
    for i  in  range (0,10,1):
        cont +=1
        print(f"{valor} X {cont} = {valor*cont}")
        sleep(.3)
    print("-" * 13)
print("fim  "*5)
