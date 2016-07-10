from random import randint

sum = 0
number = randint(1, 10000)
for c in str(number):
  sum += int(c)
print 'The number is %d.' %number
print 'The sum of its digits is %d.' %sum
