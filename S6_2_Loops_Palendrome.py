# find digits, sum of digits, reverse and paledrome in a number via a loop
x = n = int(input ('Integer: '))
count = 0
sum = 0
rev = ''
while x > 0:
    r = (x % 10)
    sum += r
    rev += str(r)
    x = x // 10
    count += 1
if int(rev) == n:
    pal = True
else:
    pal = False
print ('number of digits in ', n, ' is ', count) 
print ('Sum of digits in ', n, ' is ', sum) 
print ('Reverse of digits in ', n, ' is ', rev) 
print (n, ' is palendrome is ', str(pal))