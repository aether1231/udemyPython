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