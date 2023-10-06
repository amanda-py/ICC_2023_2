import math as m

#distancia entre dois pontos
x1, y1 = input().split()
x2, y2 = input().split()
x1,y1,x2,y2 = [float(x1),float(y1),float(x2),float(y2)]

distancia = m.sqrt((x2-x1)**2 + (y2-y1)**2)

#leitura de numeros complexos
d = complex(input())
z = m.sqrt((d.real**2)+(d.imag**2))

print("{:.4f}".format(distancia))
print("{:.4f}".format(z))