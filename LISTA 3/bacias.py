n = int(input())

#abrindo listas dos dados com todas as informações
dados = []

nome = 0
area = 1
iv_ver = 2
iv_out = 3
iv_inv = 4
iv_pri = 5

maximo = []
minimo = []
media = []

#determinando os dados referentes a cada bacia
for i in range(n):
    a = input().split()
    dados.append(a)
    for j in range(1,6):
        dados[i][j] = float(dados[i][j])

        
#retorna a posição da sublista do máximo valor encontrado
for i in dados:
    x = max(i[1:6]) #lista o maximo de cada sublista
    maximo.append(x)
    # para a posição do meu máximo (que me retorna a sublista i)
    
    
    # agora, para os mínimos:
    z = min(i[1:6])
    minimo.append(z)
    
    
    m = i[1]
    media.append(m)
    
y = maximo.index(max(maximo))
w = minimo.index(min(minimo))

#agora, dado a posição do nosso y, podemos descobrir o nome da bacia
print(dados[y][0]) # bh com os maiores indices
print(dados[w][0]) # bh com os menores indices
print('{:.2f}'.format(sum(media)/len(media)))

