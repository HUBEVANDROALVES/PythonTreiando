vel = int(input('Digite a velocidade: '))
if vel > 80:
    multa = (vel-80)*7
    print('Voce utrapassou o limite de velocidade')
    print('Sua multa é de R$: {}{}'.format('\033[4;31m',multa))
else:
    print('Voce esta dentro do limite de velocidade!!! ')