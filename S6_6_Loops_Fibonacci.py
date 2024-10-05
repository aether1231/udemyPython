# # generate Fibonacci series
n = int(input('How many terms: '))
a = 0
b = 1
s = p = ''
for i in range(n):
    s += str(a) + p
    p = ', '
    c = a + b
    a = b
    b = c
print(s.strip(', '))