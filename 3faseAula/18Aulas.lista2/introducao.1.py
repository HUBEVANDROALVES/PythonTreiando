pessoas=[["joao",19],["Ana",33],["joaquim",13],['maria', 45]]

print(pessoas)
print(pessoas[0][0])
print(pessoas[1][1])
print(pessoas[2][0])
print(pessoas[1])
print(pessoas[0][0][0])
teste=list()
teste.append('gustavo')
teste.append(40)
galera = list()
teste[0] = 'maria'
teste[1] = 22
print(galera)
print(teste)
galera = [["joao",19],["Ana",33],["joaquim",13],['maria', 45]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')