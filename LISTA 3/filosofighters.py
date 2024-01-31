num_filosofos = int(input())
filosofos = [0] # para a sequencia ficar correta 1,2,3,4 etc
lutas = []

for i in range(num_filosofos):
    identificador, nome = input().split()
    identificador = int(identificador)
    #não sei se mexo com tuplas ou dicionário ainda. mas até o momento, deixarei como túplas
    id_filosofos.append((identificador, nome))
    
for i in range(num_filosofos - 1):
    id_luta, lutador_1, lutador_2, vencedor = map(int, input().split())
    #também não tenho certeza do que usar, na dúvida vou fazer túplas
    #dicionários seriam mais fáceis?
    #o que eu devo fazer com esses resultados?
    lutas.append([id_luta, lutador_1, lutador_2, vencedor])

finish_him, vencedor_final = input().split()


    
print(filosofos, lutas)
