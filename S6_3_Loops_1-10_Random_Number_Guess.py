# guess random number between 1 and 10
import random as rand

r = rand.randint(1, 10)
correct = False
while correct == False:
    x = int(input ('Guess number: '))
    if x == r:
        correct = True
    elif x > r:
        print ('Too large')
    else:
        print ('Too small')