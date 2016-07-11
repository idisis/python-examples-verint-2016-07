from sys import argv

if len(argv) != 3:
    print 'Usage:\n%s [a] [b]' %argv[0]
    exit()

try:
  a = int(argv[1])
  b = int(argv[2])
  print 'The sum of %d and %d is %d.' %(a, b, a+b)
except ValueError:
  print 'The parameters \'a\' and \'b\' must be integers.'