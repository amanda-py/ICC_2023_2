entrada = int(input())
valor = entrada%2

if (valor==0):
    print(f'{entrada} é par')
else:
    print(f'{entrada} é ímpar')
    
print(entrada+2)