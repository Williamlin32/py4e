fname = input('Enter the name of the file: ')
fhand = open(fname + '.txt')


count = 0
for line in fhand:
    words = line.split()
    if len(words) < 2 : continue
    if words[0] != 'From' : continue
    print(words[1])
    count += 1

print('There were ', count, 'lines in the file with From as the first word')