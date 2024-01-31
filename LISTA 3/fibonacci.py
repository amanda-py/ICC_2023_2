n = int(input())

# fibonacci
an = 1
a_n = 1

if n == 1 or n == 2:
    Fn = 1
    print(Fn, end= " ")

else:
    count=3
    while count <= n:
        Fn = an + a_n
        a_n = an
        an = Fn
        count += 1

    print(Fn, end=" ")
    

# fatorial
f = 1

if n == 1 or n == 0 :
    f = 1
    print(f)
    
else:
    for i in range(1,n+1):
        f = f*i
    print(f, end=" ")


if Fn%2 == 0:
    print(a_n)