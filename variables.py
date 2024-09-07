import math

a = 123250768
b = -1.124e5
c = 12e4
d = 0b1011
e = 0o17
f = 0xff
g = '0xff'
h = 17.1
j = 17.51

# Base integers
print ('\n\r')
print ('Base integers\n')
print ('Binary number: ' + str(d))
print ('Octal number: ' + str(e))
print ('Hexadecimal number: ' + str(f))
print ('Base literal conversion: ' + str(int(g, 16)))
print ('Base 10 to Binary: ' + str(bin(a)))
print ('Base 10 to Octal: ' + str(oct(a)))
print ('Base 10 to Hex: ' + str(hex(a)))

# Type conversions
print ('\nType conversions\n')
print('Integer to boolean ' + str(a) + ': ' + str(bool(a)))
print('Integer to float ' + str(a) + ': ' + str(float(a)))
print('Integer to complex ' + str(a) + ': ' + str(complex(a)))
print('Float to boolean ' + str(b) + ': ' + str(bool(b)))
print('Float to integer ' + str(h) + ': ' + str(int(h)))
print('Float to integer ' + str(j) + ': ' + str(int(j)))
print('Float to complex ' + str(b) + ': ' + str(complex(b)))

# Scientific integers
print ('\nScientific integers\n')
print('-1.124e5 ' + ' = ' + str(b))
print ('Scientific type: ' + str(b) + ' = '+ str(type(b)))
print ('Scientific type: ' + str(c) + ' = '+ str(type(c)))

# Useful functions
print ('\nUseful functions\n')
print('Size of ' + str(a) + ': ' + str(a.__sizeof__()))
print('Type of ' + str(a) + ': ' + str(type(a)))

# Copmlex mumbers
a = 1 + 3j
b = 2 + 1j
c = complex(1, 1)

print ('\nCopmlex mumbers\n')
print ('Complex number: ' + str(c))
print ('Complex type: ' + str(a) + ' = '+ str(type(a)))
print ('Complex real: ' + str(a) + ' = '+ str(a.real))
print ('Complex img: ' + str(a) + ' = '+ str(a.imag))
print ('Complex modulus: ' + str(a) + ' = '+ str(abs(a)))
print ('Complex argument: ' + str(a) + ' = '+ str(math.atan(a.imag/a.real)))
print ('Complex conjugate: ' + str(a) + ' = '+ str(a.conjugate()))
print ('Complex addition: ' + str(a) + ' + ' + str(b) + ' = '+ str(a + b))