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

# determine factors of number
n = int(input('Enter number: '))
if n == 1:
    s = ''
else:
    s = '1, '
for x in range(2, n):
    if (n % x == 0):
        s += str(x) + ', '
print (s + str(n))

# determine if number is prime
n = int(input('Enter number: '))
p = 0
for x in range (1, n + 1):
    if (n % x == 0):
        p += 1
if (p == 2):
    print (str(n) + ' is prime')
else:
    print (str(n) + ' is not prime')