a, b = map(int, input().split())

if a==0 and b==0:
    print(a, b, 'errados')

elif b-a==0 or b-a==1:
    print(a, b, "ok")
    
else:
    print(a, b, "errados")