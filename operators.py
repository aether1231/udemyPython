import math

a = 15
b = 4
c = 1.2
d = -15

print('Floor division: ' + str(a) + '//' + str(b) + ' = ' + str(a//b))
print('Float power: ' + str(a) + '**' + str(c) + ' = ' + str(a**c))
print('Float power: ' + str(d) + '**' + str(c) + ' = ' + str(d**c))

# area of circle radius r
r = float(input ('Radius: '))
print ('Circle of radius ' + str(r) + ' has area ' + str(math.pi * r**2))

# area of cuboid 
l = float(input ('Length: '))
w = float(input ('Width: '))
h = float(input ('Height: '))
print ('Surface area of cuboid ' + str(l) + ' x ' + str(w) + ' x ' + str(h) + ' = ' + str(2 * ((l * w) + (l * h) + (w * h))))

# roots of quadratic
a = float(input ('a: '))
b = float(input ('b: '))
c = float(input ('c: '))
d = b**2 - (4 * a * c)
e = math.sqrt(math.fabs(d))
if d < 0: 
    f = complex(0, e)
else:
    f = e
r1 = (-b + f) / (2 * a)
r2 = (-b - f) / (2 * a)
print ('Roots of ' + str(a) + 'x**2 + ' + str(b) + 'x + ' + str(c) + ' = 0 are:\n\n' + str(complex(round(r1.real, 4), round(r1.imag, 4))) + '\n' + str(str(complex(round(r2.real, 4), round(r2.imag, 4)))))