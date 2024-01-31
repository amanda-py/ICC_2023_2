n = int(input())
l = []

for i in range(n):
    caminho, t1, t2, t3, t4 = input().split()
    l.append(( caminho,
               t1,
               t2,
               t3,
               t4  ))

busca = input().split()

for i in l:
    for j in i[1:]:
        if j in busca:
            print(i[0])
            break