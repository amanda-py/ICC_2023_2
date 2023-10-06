a = float(input())
b = float(input())
c = float(input())

if a < b:
    b, a = a, b
if a < c:
    c, a = a, c

'''x = float(input())
y = float(input())
z = float(input())
'''
'''f = [x,y,z]
f.sort()

a = f[2]
b = f[1]
c = f[0]
'''
''' 
uma outra possibilidade de reordenar os valores, podemos fazer:
if a < b:
    b, a = a, b
if a < c:
    c, a = a, c
'''

if a >= (b+c):
    print("NAO FORMA TRIANGULO")

elif a**2 == b**2 + c**2:
    print("TRIANGULO RETANGULO")

elif a == b == c :
    print("TRIANGULO EQUILATERO")

elif a == b or a == c or b == c:
    print("TRIANGULO ISOSCELES")

else:
    print("TRIANGULO ACUTANGULO OU OBTUSANGULO")
