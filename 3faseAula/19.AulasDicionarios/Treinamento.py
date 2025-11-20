dados=dict()
dados = {"nome":"pedro","idade":25}# cria o dicionario

print(dados['nome'])
print(dados['idade'])
dados["sexo"]="M"

print(dados)

filmes = {"Titulo":"star wars","ano":"1977","Diretor":"George Lucas","tipo":"Ficção"}
print(filmes.values())## IMPRIME VALORES
print(filmes.keys())## IMPRIME TITULOS
print(filmes.items())### IMPRIME TUDO

for k,v in filmes.items():
    print(f"O {k}  é {v}")
pessoa = {"nome":"pedro","idade":25, "Sexo":"m"}
print(pessoa)
del pessoa['Sexo'] ## DELETA O SEXO 
pessoa["nome"]="leandro"##  TROCA O NOME
print(pessoa)