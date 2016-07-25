from sys import argv
from sys import stdout
from collections import defaultdict
from collections import Counter

filename = argv[1]
words = defaultdict(list)

# parse hosts file:
with open(filename, 'r') as inputFile:
    for line in inputFile:
        if line[-1] == '\n':
            line = line[:-1]
        letterCount = Counter(sorted(line.lower()))
        words[letterCount.__str__()].append(line)

for list in words.itervalues():
    for word in list:
        stdout.write(word)
        stdout.write(' ')
    stdout.write('\n')
