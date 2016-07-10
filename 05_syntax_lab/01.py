print 'Enter 10 integers, 1 in each line:'
biggest = int(raw_input())
for i in range(9):
  number = int(raw_input())
  biggest = max(number, biggest)
print biggest 
