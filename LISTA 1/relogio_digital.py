entrada = int(input())

horas = entrada//3600
minutos = (entrada%3600)//60
segundos = (entrada%3600)%60

print('{}h:{}m:{}s'.format(horas, minutos, segundos))