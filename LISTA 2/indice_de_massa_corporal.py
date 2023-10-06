p = float(input())
h = float(input())

imc = p/(h**2)
correcao = p - 24.9*h**2

print('{:.2f}'.format(imc))

if imc < 18.5:
    print("Baixo peso")
    
elif 18.5<= imc <= 24.9:
    print("Peso normal")
    
elif 24.9< imc <=29.9:
    print("Sobrepeso")
    print('{:.2f}'.format(correcao))
    
elif 29.9 < imc <= 34.9:
    print("Obesidade grau I")
    print('{:.2f}'.format(correcao))
    
elif 34.9 < imc <= 39.9:
    print("Obesidade grau II")
    print('{:.2f}'.format(correcao))
    
elif imc > 39.9:
    print("Obesidade grau III")
    print('{:.2f}'.format(correcao))
