'''
            Metros para Pés:

Sabendo que o pé equivale a 0.3048 metros, faça um programa que leia uma medida em pés e imprima o valor em metros.

Entrada:
  Leia um número real do teclado, que corresponde a medida em pés.

Saída:
  Imprima na tela o valor em metros, com duas casas decimais após a vírgula.


'''

x = float(input())          # pés
y = x*0.3048                # dados em metros

print("{:.2f}".format(y))
