x = int(input())

cem = x//100
cinquenta = (x%100)//50
vinte = ((x%100)%50)//20
dez = (((x%100)%50)%20)//10
cinco = ((((x%100)%50)%20)%10)//5
dois = (((((x%100)%50)%20)%10)%5)//2
um = ((((((x%100)%50)%20)%10)%5)%2)//1

'''
1.será que posso fazer isso com for?
2.usar um encurtamento para o print 
'''

print(x)
print(f"{cem} nota(s) de R$ 100,00")
print(f"{cinquenta} nota(s) de R$ 50,00")
print(f"{vinte} nota(s) de R$ 20,00")
print(f"{dez} nota(s) de R$ 10,00")
print(f"{cinco} nota(s) de R$ 5,00")
print(f"{dois} nota(s) de R$ 2,00")
print(f"{um} nota(s) de R$ 1,00")