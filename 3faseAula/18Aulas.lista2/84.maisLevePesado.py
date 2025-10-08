#ler varios nomes e peso e mostra mais leve e mais pesado
# e a quantidade de pessoas cadastras
dados=list()
nomes=list()
while True:
    nome = input("Digite o nome( ou 'fim' para parar) :  ")
    if nome.lower() == "fim":
        break
    peso = float(input("Digite a peso: "))

    dados.append(nome)
    dados.append(peso)
    nomes.append(dados[:])
    dados.clear()
mais=menos=nomes[0][1]
for p in nomes:
    if p[1] > mais:
        mais = p[1]
    if p[1] < menos:
        menos = p[1]

print(f"\n Total de pessoas cadastrados foi {len(nomes)}")
print(f'O Maior peso foi {mais} Kg. Pertence a: ', end=' ')
for p in nomes:
    if p[1] == mais:
        print(p[0], end=" ")
print(f"\nO Menor peso foi {menos} pertencente a :", end=" ")
for p in nomes:
    if p[1] == menos:
        print(p[0], end=" ")




