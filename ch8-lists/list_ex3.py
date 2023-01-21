fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    # print 'Debug:', words
    if words[0] != 'From' or len(words) < 3  : continue
    print(words[2])