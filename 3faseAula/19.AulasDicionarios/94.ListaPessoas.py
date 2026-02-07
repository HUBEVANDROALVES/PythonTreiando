#lista nome,sexo e idade
#criar dicionairo
#mostrar qtd pessoa, Media idade, lista mulheree
#lista homes/
#lista de todas as pessoa com idade acima da media.

pessoas=[]
mulheres=[]
cont=somaidade=media=0
while True:
    pessoa = {}
    pessoa["nome"]=input("Digite o nome da pessoa:")
    pessoa["sexo"]=input("Digite o Sexo da pessoa M/F: ").upper()
    pessoa["idade"]=int(input("Digite a idade: "))
    pessoas.append(pessoa.copy())
    somaidade += pessoa["idade"]

    if pessoa["sexo"] == "F":
        mulheres.append(pessoa["nome"])

    sair =input("Deseja encerra S/N:").upper()
    if sair == "S":
        break
    media= somaidade / len(pessoas)


print(f"\nA-Total de pessoas: {len(pessoas)}")
print(f"B-Média de idade:{media:.2f}")
print(f"C-As mulheres cadastradas foram:{mulheres}")

print("\nPessoas acima da media:")
for p in pessoas:
    if p["idade"] > media:
        print(p["nome"], p["idade"])