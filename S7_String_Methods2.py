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