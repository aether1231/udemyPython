# get methods of string class
s = 'Hello, how are you'
print(dir(str))

# get help for class methods
print(help(s.endswith))

# find/index starting index of substring
print(s.find('how'))
print(s.index('how'))

# find/index starting index of substring with optional start and end search indices
print(s.find('how', 0, 9))
#print(s.index('how', 0, 9)) # trows error if not found rathar than -1

# rfind/rindex starting index of substring
print(s.rfind('how'))
print(s.rindex('how'))

# count how many times substring occurs
print(s.count('o'))

# ljust/rjust/center
print(s.ljust(30))
print(s.rjust(30, '_'))
print(s.center(30, '-'))

# strip, lstrip, rstrip
print(s.center(30).strip())
print(s.rjust(30, '_').lstrip('_'))
print(s.center(30, '_').rstrip('_'))

# strip multiple characters
s1 = '_*+_. ' + s + '_*+_. '[: : -1]
print(s1)
print(s1.strip('._+* '))

# capitalize/title
s1 = 'how are you dear'
print(s1.capitalize())
print(s1.title())

# upper/lower
s1 = 'hoW ArE yOu deAr'
print(s1.lower())
print(s1.upper())

# swapcase
print('hElLO WorLD'.swapcase())

# inquiry string functions
print("'hElLO WorLD'.isupper(): ", 'hElLO WorLD'.isupper())
print("'hello world'.islower(): ", 'hello world'.islower())
print("'Hello World'.istitle(): ", 'Hello World'.istitle())
print("'acbdef'.isalnum(): ", 'abcdef'.isalnum())
print("'acbd f'.isalnum(): ", 'abcd f'.isalnum())
print("'abc123'.isalnum(): ", 'abc123'.isalnum())
print("'abc123'.isalpha(): ", 'abc123'.isalpha())
print("'      '.isspace(): ", '      '.isspace())
print("'.     '.isspace(): ", '.     '.isspace())
print("'abc123'.isascii(): ", 'abc123'.isascii())
print("'abc123'.isidentifier(): ", 'abc123'.isidentifier())     # valid variable name
print("'123abc'.isidentifier(): ", '123abc'.isidentifier())     # valid variable name
print("'123abc'.isprintable(): ", '123abc'.isprintable())
print("'123\\tbc'.isprintable(): ", '123\tbc'.isprintable())
print("'12345'.isdecimal(): ", '12345'.isdecimal())
print("'123.45'.isdecimal(): ", '123.45'.isdecimal())
print("'0xff00'.isdecimal(): ", '0xff00'.isdecimal())
print("'0o7600'.isdecimal(): ", '0o7600'.isdecimal())
print("'12345'.isdigit(): ", '12345'.isdigit())
print("'123.45'.isdigit(): ", '123.45'.isdigit())
print("'12345'.isnumeric(): ", '12345'.isnumeric())
print("'123.45'.isnumeric(): ", '123.45'.isnumeric())