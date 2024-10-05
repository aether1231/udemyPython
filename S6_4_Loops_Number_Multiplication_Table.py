# display multiplication table for given number
n = int(input ('number: '))
for x in range (1, 13):
    print (str(x), ' x ', str(n), ' = ', str(x * n))

# find the factorial of a number
f = 1
for x in range (1, n + 1):
    f = f * x
print ('!', str(n), ' = ', str(f))