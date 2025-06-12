dista = int(input('Digite a distancia da viagem: '))
if dista <= 200:
    valor = dista*0.50
    cor = '\033[33m'
else:
    valor = dista*0.45
    cor = '\033[32m'
print ('O valor a ser pago é R$ {}{:.2f} ' .format(cor,valor))