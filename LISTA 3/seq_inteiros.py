n = None
l = []

while n != 0:
    n = int(input())
    l.append(n)

l.remove(0)

if l == []:
    l = [0]
    tamanho = 0
    print(0)

else:
    print(len(l))

print(max(l))
print('{:.2f}'.format(sum(l)/(len(l))))