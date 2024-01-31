n = int(input())
l = []
contador = 0
for i in range(n):
    l.append(input().split())

#print(l)

for i in l:
    #i é cada linha
    if i == l[-1]:
        break
    for j in i:
        # j é cada elemento
        
        k = i.index(j)
        m = l.index(i)
        if j == 'o' and (l[m+1][k] == '.' or l[m+1][k] == 'o'):
            l[m][k] = '.'
            l[m+1][k] = 'o'
print(l)
    
    

#######################
'''
    
for i in range(n):
    if 'x' in l[-1]:
        if i != n - 2:
            for j in l[i]:
                if j == 'o':
                    a = l[i].index('o')
                    l[i][a] = '.'
                    l[i+1][a] = 'o'
    else:
        for j in l[i]:
                if j == 'o':
                    a = l[i].index('o')
                    l[i][a] = '.'
                    l[i+1][a] = 'o'
    print(' '.join(l[i]))
'''