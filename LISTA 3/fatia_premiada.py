fatias, premiada = map(int, input().split())
l = list(range(fatias))

for i in range(fatias):
    nome, comeu = input().split()
    comeu = int(comeu)
    
    if l.pop(comeu) != premiada:
        continue
    else:
        ganhador = nome
        
print(ganhador)