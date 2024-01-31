frase = input().lower().split()
frase_final= []

contador_palavras = {}

pontuacao = ['.', ',', '?', '!', ':']


for i in frase:
    for j in i:
        if j in pontuacao:
            i = i.replace(j,'')
            
    frase_final.append(i)
    contador_palavras[i] = frase_final.count(i)


contador_palavras = dict(sorted(contador_palavras.items(), key=lambda x: (x[1],x[0])))

contador_palavras = dict(reversed(contador_palavras.items()))


for key, value in contador_palavras.items():
    key = key.replace(key, key.capitalize())
    print(key, value)

