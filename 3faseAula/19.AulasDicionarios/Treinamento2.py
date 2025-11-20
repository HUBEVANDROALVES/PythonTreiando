brasil = []
estado1 = {"uf":"Rio de Janeiro","sigla": "RJ"}
estado2 = {"uf":"Sao paulo", "sigra":"SP"}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[0:])
print(brasil[0]['uf'])

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf']=str(input("Unidade Federativa: "))
    estado['sigla']=str(input("Sigla do Estado: "))
    estado['Regiao']=str(input("Qual a regiao: "))
    brasil.append(estado.copy()) # cria a copia
for e in brasil:
    for v, k in e.items():
        print(f"O Campo  {v} tem o valor {k}.")
    for b in e.values():
        print(b, end=" ")
    print()
