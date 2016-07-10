from random import randint
num1 = randint(1, 10)
num2 = randint(1, 10)

print 'The numbers are: %d, %d.' %(num1, num2)
for i in range(max(num1, num2), num1 * num2 + 1):
  if i % num1 == 0 and i % num2 == 0:
      print 'The result is %d.' %i
      break
