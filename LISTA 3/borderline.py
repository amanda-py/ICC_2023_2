n = int(input())
l = []

for i in range(n):
    wrd_1, wrd_2 = input().split()
    l.append((wrd_1, wrd_2))

frase_amigos = input().split()
frase_final = []

for i in frase_amigos:
    for j in l:
        if i == j[0]:
            frase_final.append(j[1])
            
if frase_final == []:
    print('Tudo bem!')
    
else:
    print(' '.join(frase_final))
'''
for i in l[::-1]:
    for j in i:
        if j in frase_amigos:
            frase_final.append(i[1])
            
if frase_final == []:
    print('Tudo bem!')
    
else:
    print(' '.join(frase_final))'''