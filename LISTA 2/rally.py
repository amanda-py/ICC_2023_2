t1, vt1, t2, vt2 = map(int, input().split())

# tempo em segundos

vx1 = 0
vx2 = 0

if t1 > 1800:
    x1 = 1800 - t1

if t1 < 1800:
    x1 = 2*(t1 - 1800)
    
if vt1 > 60:
    vx1 = 10*(60 - vt1)

if t2 > 3600:
    x2 = 3600 - t2

if t2 < 3600:
    x2 = 2*(t2 - 3600)

if vt2 > 40:
    vx2 = 20*(40 - vt2)

print(x1)
print(x1 + vx1)
print(x2)
print(x2 + vx2)
print(x1 + x2)
print(x1 + x2 + vx1 + vx2)
