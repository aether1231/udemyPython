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