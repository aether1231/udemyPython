# Reverse a string
x = 'Hello World'
l = len(x)
print(x[l: 0: -1])

# Implicit 0 start index
print(x[: len(x): 1])

# Implicit 0 start and end index
print(x[: : 1])

# Implicit 0 start, end and increment
print(x[: :])

# Implicit reverse with negative increment
print(x[: : -1])

# Presence
print(str('Z' not in x))