dias=int(input('Quantos dias de aluguel ?  '))
km = int(input( 'Quantos kilomentro rodado ?  '))
valor = dias*60 + km* 0.15

print('O valor do aluguel por {} Dias com {}KM rodado é R$ {:.2f} '.format(dias,km,valor))