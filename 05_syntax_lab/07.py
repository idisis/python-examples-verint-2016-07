from random import randint
number = randint(1, 100)

print 'I\'m thinking of a number between 1 and 100...'
while True:
  guess = int(raw_input('take a guess: '))
  if (guess == number):
      print 'that\'s right!'
      break
  print 'a little bit %s...' %('higher' if guess < number or randint(0, 9) == 0 else 'lower')

