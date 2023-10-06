'''
carro bebe 14.2km/l
'''

t = float(input()) 	#tempo gasto
v = float(input()) 	#velocidade média

dist = t*v			#km
litros = dist/14.2

print(dist,"{:.2f}".format(litros))