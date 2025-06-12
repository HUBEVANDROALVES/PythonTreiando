import math
import random
jokenpo=input('Escolha: \n A)Pedra \n B)Papel \n C)Tesoura  \n')
jokenpo1=random.randint(1,3)
if jokenpo=='a' and jokenpo1==3:
    print('Voce ganhou')
elif jokenpo=='b' and jokenpo1==1:
    print('Voce Ganhou')
elif jokenpo=='C' and jokenpo1==2:
    print('Voce Ganhou')
elif jokenpo=='a' and jokenpo1==1:
         print('Voce empatou')
elif  jokenpo=='b' and jokenpo1==2:
         print('Voce empatou')
elif  jokenpo1=='c' and jokenpo1==3:
         print('Voce empatou')
else:
     print('Voce perdeu')
     print (jokenpo1)

