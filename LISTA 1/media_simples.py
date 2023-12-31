'''
Média Simples

Faça um programa que peça ao usuário para informar dois números reais, conforme especiﬁcado em Entrada. Depois calcule a média desses números e mostre-a na tela, conforme especiﬁcado em Saída.

Entrada:

Leia 2 números reais do teclado, um por linha.

Saída:

Imprima na tela media, onde media é um real com duas casas decimais que representa a média dos dois reais lidos do teclado.

Comentários: 

Lembre-se que para ler um número em uma linha, use input( ). Porém, input lê apenas strings do teclado, portanto você deverá converter as strings em float (ponto flutuante). No exemplo a seguir, o usuário digita dois números um por linha, então, o programa lê cada número como string e o converte para ponto flutuante:

A = float(input( ))

B = float(input( ))

O comando print( ) pode ser usado para imprimir na tela o resultado da média.  Três exemplos de como imprimir um valor C com duas casas decimais:

print(“%.2f” % C)

print(“{:.2f}”.format(C))

print(f"{C:.2f}")

'''

a = float(input())
b = float(input())

media = (a+b)/2

print("{:.2f}".format(media))
