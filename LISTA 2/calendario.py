'''
d: dia da semana correspondente ao primeiro
dia do mes; 1 é segunda, 2 terça, até 7 domingo'''

m, d = map(int, input().split())

m_31 = [1, 3, 5, 7, 8, 10, 12]
m_30 = [4, 6, 9, 11]
m_jan = [2]
colunas = 0
#nos casos dos meses com 31 dias:
if m in m_31:
    if d==6 or d==7:
        colunas = 6
    else:
        colunas = 5
elif m in m_30:
    if d==7:
        colunas = 6
    else:
        colunas =5
else:
    if d==7:
        colunas = 5
    else:
        colunas = 4
print(colunas)
