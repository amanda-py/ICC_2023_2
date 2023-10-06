cargo = str(input())
tempo_serv = int(input())
sal_atual = float(input())

reajuste = 0



#GERENTE:
if cargo == 'Gerente':
	if tempo_serv <= 3:
		reajuste = 0.12
		
	elif tempo_serv <=6:
		reajuste = 0.13
		
	elif tempo_serv > 6:
		reajuste = 0.15
		

#ENGENHEIRO
elif cargo == 'Engenheiro':
	if tempo_serv <= 3:
		reajuste = 0.07
		
	elif tempo_serv <=6:
		reajuste = 0.11
		
	elif tempo_serv > 6:
		reajuste = 0.14
		

#OUTROS
else:
	if tempo_serv <= 3:
		reajuste = 0.05
		
	elif tempo_serv <=6:
		reajuste = 0.05
		
	elif tempo_serv > 6:
		reajuste = 0.05

if sal_atual < 1039:
	print('Salário inválido!')
else:
	print('{:.2f}'.format(reajuste*sal_atual))
	print('{:.2f}'.format(sal_atual*(1+reajuste)))
	
# a saída está errada, como coloco esses poucos prints dentro desse loop com a condição lá de cima?
#eu pensei em usar while sal_atual =>1039: (colocar as condições de if dentro), ou um if maior
#acreduto que um if será mais efetivo