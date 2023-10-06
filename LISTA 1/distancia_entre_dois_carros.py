velx = 60	#km/h
vely = 75	#km/h

'''
x = velxt
y = velyt
x - y = distancia
(x-y)/(velx-vely)=t'''

dist_xy = float(input())

t = int((dist_xy/(vely-velx))*60)

print(t, "minutos")