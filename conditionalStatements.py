# if, elif, else
i = int(input('Enter integer: '))
if (i > 0):
    print (str(i), ' is positive')
elif (i < 0):
    print (str(i), ' is negative')
else:
    print (str(i), ' is zero')

# diffrence between numbers
n1 = int(input('Enter integer: '))
n2 = int(input('Enter integer: '))
if n1 > n2:
    result = n1 - n2
else:
    result = n2 - n1
print ('Differnce is ', str(result))

# odd or even
if i % 2:
    print (str(i), ' is odd')
else:
    print (str(i), ' is even')

# vote eligibility
if i >= 18:
    print('Vote eligible')
else:
    print('Vote ineligible')

# pass mark validity
if (i >= 0) and (i <= 100):
    print('Valid')
else:
    print('Invalid')

# pass mark
m = int(input('Enter maths: '))
p = int(input('Enter physics: '))
c = int(input('Enter chemistry: '))
if m >= 45 and p >= 45 and c >= 45:
    print ('Pass')
else:
    print ('Fail')

# authorised users
name = input ('Name: ').lower()
if name == 'john' or name == 'smith':
    print ('Authorised')
else:
    print ('Unauthorised')

# consonant
vowel = ['a', 'e', 'i', 'o', 'u']
if len(name) == 1:
    if name in vowel:
        print ('Vowel')
    else:
        print ('Consonant')
else:
    print ('Invalid')
