import argparse 

parser = argparse.ArgumentParser(description='Combine two text files with interleave.')
parser.add_argument('a', help='first file.')
parser.add_argument('b', help='second file.')
parser.add_argument('o', help='Output file.')
args = parser.parse_args()

with open(args.a, 'r') as a:
  with open(args.b, 'r') as b:
    with open(args.o, 'w') as o:
        for line in a:
            o.write(line)
            if line[-1] != '\n':
            	print >> o, ""
        for line in b:
            o.write(line)
            if line[-1] != '\n':
            	print >> o, ""