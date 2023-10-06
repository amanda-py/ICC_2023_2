a = 1
y = 0
while(a<6):
    e = float(input())
    x = a * e
    y = y + x
    a = a + 1

media = y/15

print("{:.3f}".format(media))

'''
usando o for:
y=0
for i in range(1,7):
    x = float(input())
    y = y +x*i
'''