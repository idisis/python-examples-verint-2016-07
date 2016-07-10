from random import randint

sum = int(0)
for i in range(7):
  sum += randint(1, 100)
print sum
if sum % 7 == 0: print 'Boom'