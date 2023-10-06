compra, parcela = map(float, input().split())

if (parcela==1):
    valor = compra - compra*0.05
    print('{:.2f} {:.2f}'.format(valor, valor/parcela))
elif (parcela==2):
    valor = compra
    print('{:.2f} {:.2f}'.format(valor, compra/2))
elif (parcela==3):
    valor = compra + compra*0.05
    print('{:.2f} {:.2f}'.format(valor, valor/3))
elif (parcela==4):
    valor = compra + compra*0.1
    print('{:.2f} {:.2f}'.format(valor, valor/4))