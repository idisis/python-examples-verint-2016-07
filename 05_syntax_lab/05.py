from random import randint

while True:
    number = randint(1, 1000000)
    if number % (7*13*15) == 0: break
print 'The number is %d.' %number
