n = int(input())
l = []

for i in range(n):
    nome, posicao = input().split()
    l.append((posicao, nome))

l.sort()
if len(l)>1:
    if l[-1][0] == l[-2][0]:
        print(l[-2][1])
    else:
        print(l[-1][1])
else:
    print(l[0][1])