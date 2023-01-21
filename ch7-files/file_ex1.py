fhand = open('testing.txt')
count = 0 
for line in fhand:
    line = line.rstrip()
    count = count + 1
    print(count, line)