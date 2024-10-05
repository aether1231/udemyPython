# generate arithmetic progression
a = int(input('a: '))
d = int(input('d: '))
n = int(input('n: '))
s = ''
for x in range(a, a + n * d + 1, d):
    if x != a + n * d:
        s += str(x) + ', '
    else:
        s += str(x)
print (s)