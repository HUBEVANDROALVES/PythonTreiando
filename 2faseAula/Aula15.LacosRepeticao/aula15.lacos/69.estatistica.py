

homem=mulher=demaior=mulher20=0
SimNao= " "
while True:
    print("-" * 20)
    print("CADASTRE UMA PESSOA")
    print("-" * 20)
    idade = int(input("Idade: "))
    sexo = input("Sexo: [M/F] ").upper().strip()[0]
    if idade >= 18:
        demaior += 1
    if sexo == "F":
        mulher += 1
        if  idade > 20:
            mulher20 += 1
    if sexo == "M":
        homem += 1
    SimNao=input("Deseja continuar ? [S/N]").upper().strip()[0]
    if SimNao == "N":
        break
print("-="*20)
print(f"Total de pessoas com mais de 18 Anos: {demaior} \nAo todo temos {homem} Homens cadastrados \nE temos {mulher} mulheres  cadastradas sendo {mulher20} com mais de 20 anos")
