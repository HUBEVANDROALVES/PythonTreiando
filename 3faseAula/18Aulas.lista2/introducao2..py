nomes=list()
dado=list()
contMaior=0
contMenor=0
for i in range(0,5):
    dado.append(str(input("Digite o nome: ")))
    dado.append(int(input("Digite a idade: ")))
    nomes.append(dado[:])
    dado.clear()
for p in nomes:
    if p[1] >= 21:
        print (f"{p[0]} é maior de idade. ")
        contMaior += 1
    else:
        print (f"{p[0]} é menor de idade.")
        contMenor += 1

print()
print(f"temos {contMenor} de memores e {contMaior} de maior.")
