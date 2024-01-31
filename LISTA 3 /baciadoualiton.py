n = int(input())

areas = 0

pluv_max = -1
nome_max = None
pluv_min = -1
nome_min = None

for i in range(n):
    ent = input().split()
    areas += float(ent[1])

    sub = [float(elem) for elem in ent[2:]]
    if sum(sub) > pluv_max:
        pluv_max = sum(sub)
        nome_max = ent[0]
    if min(sub) < pluv_min or pluv_min == -1:
        pluv_min = min(sub)
        nome_min = ent[0]

print(nome_max)
print(nome_min)
print("{:.2f}".format(areas/n))
