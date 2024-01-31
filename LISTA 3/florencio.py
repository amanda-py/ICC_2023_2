'''n = list(input())
alfabeto = list('abcdefghijklmnopqrstuvwxyz')

for i in n:
    
    if n[0] in alfabeto:
        n[0] = n[0].upper()
        continue
    
    if n[-1] == '_':
        del n[-1]
        continue
    
    if i == '_':
        if n[n.index(i) + 1] in alfabeto:
            n[n.index(i) + 1] = n[n.index(i) + 1].upper()
            n.remove(i)
        if not n[n.index(i) + 1] in alfabeto:
            pass
        
        
    
        
print(''.join(n))'''
###########################
n = input().split('_')
frase = ''

while '' in n:
    n.remove('')
    
for i in n:
    frase += i[0].upper() + i[1:]

print(frase)