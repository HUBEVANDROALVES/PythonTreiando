from ctypes import c_char

print("="*30)
print("{:^30}".format('BANCO HUBEVANDRO')) # TEXTO E COLOCADO E ^ (centralizado)
print("="*30) # Option (⌥) + i Depois pressione espaço → gera o ^ puro.
valor = int(input("Qual o valor que voce que sacar ?  "))
total = valor
cedular = 50
totalced = 0

while True:
    if total >= cedular:
        total -= cedular
        totalced += 1
    else:
        if totalced > 0 :
            print(f"Togal de {totalced} cédulas de  R$ {cedular}  ")
        if cedular == 50:
            cedular = 20
        elif cedular == 20:
            cedular = 10
        elif  cedular == 10:
            cedular = 1
        totalced = 0
        if total == 0 :
            break

print('='*30)
print("Volte sempre ao Banco HUBEVANDRO ! BOM DIA ")

