import math
from time import sleep


print("    Voce Vai escolhe dois numero \n e pedir o que fazer na tabela abaixo.")
sleep(1)
n1=int(input ("Digite o primeiro numero: "))
sleep(1)
n2=int(input("Digite o Segundo numero: "))
sleep(1)
escolha=0
while escolha != 5:
    escolha = int(input('Digite o que que fazer: \n [1] Somar  \n [2]Multiplicar \n [3]Maior   \n [4]Novos numeros \n [5] Sair \n Sua escolha: '))
    if escolha ==1:
        soma=n1+n2
        print ('A soma dos numeros é {}'.format(soma))

    elif escolha == 2:
        soma=n1*n2
        print( 'A Multiplicacao dos numeros  é {} '.format(soma))

    elif escolha==3:
        maior = n1 if n1 > n2 else n2
        print('O maior numero é {} '.format(maior))

    elif escolha==4:
        print  ('Informe os numeros novamente')
        n1=int(input('Digite o primeiro numero'))
        n2=int(input('Digite o segundo numero '))
    elif escolha==5:
        print('Finalizando ')
    else:
        print ( 'Opcao invalida  ' )
    print('=-=' *10)
print ('Fim do programa ! Volte sempre!')

print('Fim do programa !!!')



