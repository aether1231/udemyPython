# calculate discount amount
price = float (input ('Enter price: '))
if price <= 1000:
    print ('10%')
elif price > 1000 and price <= 5000:
    print ('20%')
elif price > 5000 and price <= 10000:
    print ('30%')
else:
    print ('50%')

# string relational operators
s1 = input ('Enter string 1: ')
s2 = input ('Enter string 2: ')
if (s1 < s2):
    print (s1, ' < ', s2)
else:
    print (s1, ' >= ', s2)

# binary operators
x = int(input ('Enter integer 1: '))
y = int(input ('Enter integer 2: '))
print (x, '(', format(x, 'b'), ') & ', y, '(', format(y, 'b'), ') = ', x & y, '(', format(x & y, 'b'), '): bits = ', (x & y).bit_length())
print (x, '(', format(x, 'b'), ') | ', y, '(', format(y, 'b'), ') = ', x | y, '(', format(x | y, 'b'), '): bits = ', (x | y).bit_length())
print (x, '(', format(x, 'b'), ') ^ ', y, '(', format(y, 'b'), ') = ', x ^ y, '(', format(x ^ y, 'b'), '): bits = ', (x ^ y).bit_length())
print (x, '(', format(x, 'b'), ') >> ', y, ' = ', x >> y, '(', format(x >> y, 'b'), '): bits = ', (x >> y).bit_length())
print (x, '(', format(x, 'b'), ') << ', y, ' = ', x << y, '(', format(x << y, 'b'), '): bits = ', (x << y).bit_length())
print ('~', x, '(', format(x, 'b'), ') = ', ~x, ' (', format(~x, 'b'), '): bits = ', (x << y).bit_length())