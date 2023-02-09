def toInt(list):
    for i in range(len(list)):
        list[i] = int(list[i])

a = input('a: ').split(' ')
b = input('b: ').split(' ')
w = int(input('w: '))
t = int(input('t: '))
C = [0] * t
e = 0

toInt(a)
toInt(b)
a.reverse()
b.reverse()

C[0] = (a[0] + b[0]) % (2 ** w)
for i in range(0, t, 1):
    C[i] = (a[i] + b[i] + e) % (2 ** w)
    if 0 < a[i] + b[i] < 2 ** w:
        e = 0
    else:
        e = 1

C.reverse()
C = tuple(C)
res = []
res.append(e)
res.append(C)
res = tuple(res)

print(res)