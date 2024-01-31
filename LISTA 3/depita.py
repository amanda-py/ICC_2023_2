n = int(input())
resultado = {}

for i in range(n):
     pedido = input()
     pedido = pedido.split()
     nome = pedido[0]
     comida = ' '.join(pedido[1:])
     resultado[nome] = comida

resultado = dict(sorted(resultado.items()))

print(len(resultado))

for valores in resultado.values():
    print(valores)
