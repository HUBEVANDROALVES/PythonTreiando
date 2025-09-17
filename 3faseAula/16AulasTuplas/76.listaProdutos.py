n1=25
cont1=0
cont=0
tuplaValor= ()
acabar=" "
tuplaProd= ()
while True:
    produto=str(input("Digite o  Produto: "))
    tuplaProd += (produto,)
    valor=float(input("Digite o valor do produto: "))
    tuplaValor += (valor,)
    print("-="*n1)
    cont1 += 1
    acabar=input("Deseja terminar Sim ou Não S/N : ").upper().strip()[0]
    print("-=" * n1)

    if acabar == "S":
        break
        cont1=0

print("-"*30)
print("\n=== Os produtos cadastrados foram ===")
for i in range(len(tuplaProd)):
    print(f"{tuplaProd[i]}{'-' * (25 - len(tuplaProd[i]))}RS {float(tuplaValor[i]):.2f}")
