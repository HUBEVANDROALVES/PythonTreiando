frase = '   Curso em video python   '

frase2 = '''Lorem Ipsum é simplesmente uma simulação de texto
da indústria de impressão e composição. Lorem Ipsum
tem sido a simulação de texto padrão da indústria
desde os anos 1500, quando um impressor desconhecido
pegou uma bandeja de tipos e a embaralhou para fazer um
livro de modelos de tipos. Sobreviveu não apenas cinco séculos,
mas também o salto para a composição eletrônica, permanecendo
essencialmente inalterado. Foi popularizada na década de.'''
texto_sujo = "   Python; Java; C++;Ruby  ;  JavaScript  "
linguagens = [lang.strip() for lang in texto_sujo.split("a")]
print("Linguagens limpas:", linguagens)
print(len(frase))
print(frase.upper().count('O'))#transforma em maiculo e mostra.
print(frase.upper())
print(len(frase.strip()))# remove os espacoes antes e depois
print(frase.replace('python', 'bordado')) # troca as palavras
print(frase)
frase = frase.replace('python', 'corte')# troca
print(frase)
print(frase.split())
dividido = (frase.split())
print(dividido[0])
print(dividido[2][0])