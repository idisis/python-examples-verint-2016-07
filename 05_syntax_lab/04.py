lines = list()
i = int(0)
while True:
  i += 1
  line = raw_input("line {}: ".format(i))
  if not line: break
  lines.append(line)
lines.reverse()
for line in lines:
  print line