s = 'python is easy'

# startswith, endswith, removeprefix, removesuffix, partion, rpartion
print("s.startswith('python'): ", s.startswith('python'))
print("s.startswith('is'): ", s.startswith('is'))
print("s.startswith('is', 7): ", s.startswith('is', 7))
print("s.endswith('easy'): ", s.endswith('easy'))
print("s.endswith('a'): ", s.endswith('a'))
print("s.removeprefix('python'): ", s.removeprefix('python'))
print("s.removesuffix('easy'): ", s.removesuffix('easy'))
print("s.partition('is'): ", s.partition('is'))
print("s.rpartition('a'): ", s.rpartition('a'))

# replace
s = 'a-b-c-d-e'
print(s, ".replace('-', ','): ", s.replace('-', ','))
print(s, ".replace('-', ',', 2): ", s.replace('-', ',', 2))

# split
print(s, ".split('-'): ", s.split('-'))
print(s, ".split('-', 2): ", s.split('-', 2))

# rsplit
print(s, ".rsplit('-', 2): ", s.rsplit('-', 2))

# join
s = ['a', 'b', 'c', 'd', 'e']
print("'\\'.join(", str(s), "): ", ','.join(s))

# linesplit
s = 'abc\ndef\thig\righ\fikl'
print(s, ".splitlines(): ", s.splitlines())

s = 'bghiamporcd'
print("sorted(s): ", sorted(s))
print("''.join(sorted(s)): ", ''.join(sorted(s)))

# Challenge 79
item = input('Item: ')
price = input('Price: ')
l = 25 - len(item) - len(price)
print(''.join([item, '.'*l, price]))

# Challenge 80
pass1 = input('Password: ')
pass2 = input('Password: ')

if (pass2 == pass1):
    print('Password accepted')
else:
    if pass1.lower() == pass2.lower():
        print('Please check cases and try again')

# Challenge 81
n = input('Input cerdit card number: ')
last4 = n[len(n) - 4: :]
print('**** ' * 3 + last4)

# Challenge 82: Find user id and domain name from email address
e = input('Enter email address: ')
f = e.split('@')
print('User id: ' + f[0] + ', Domain name: ' + f[1])

# Challenge 83: Is palendrome?
x = input('Enter string: ')
if x == x[: : -1]:
    print('String is palendrome')
else:
    print('String is NOT palendrome')
print('palendromic string is ' + x + x[: : -1])

# Challenge 84: Find day, month and year from date
d = input('Enter date: ')
a = d.split('/')
print('Day is ' + str(a[0]) + ', Month is ' + str(a[1]) + ', Year is ' + str(a[2]))

# Challenge 85: Is anagram
s1 = input('Enter word1: ')
s2 = input('Enter word2: ')
t1 = {}
t2 = {}
if (len(s1) == len(s2)):
    for x in s1:
        if x in t1:
            t1[x] += 1
        else:
            t1[x] = 1
    for y in s2:
        if y in t2:
            t2[y] += 1
        else:
            t2[y] = 1

    equal = True
    for x in t1:
        if t1[x] != t2[x]:
            equal = False
            break

    if equal:
        print(s1, 'and', s2, 'ARE anagrams')
    else:
        print(s1, 'and', s2, 'are NOT anagrams')
else:
    print(s1, 'and', s2, 'are NOT anagrams')

# Challenge 86: Rearrange string case 
s = input('Enter string: ')
lower = ''
upper = ''
for x in s:
    if x.isupper():
        upper += x
    else:
        lower += x
print(lower + upper)

# Challenge 87: Remove punctuation characters

punct = '\'[]!"£$%^&*()-+=.,/#<>?:;@~\\|\ '
s = input('Enter string: ')
o = ''
for x in s:
    if x not in punct:
        o += x
print(o)