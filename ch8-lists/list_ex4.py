
fname = input('Enter file: ')
fhand = open(fname)

wlist = []

for word in fhand:
    words = word.split()
    for w in words: 
        if w not in wlist: 
            wlist.append(w)

wlist.sort()
print(wlist)

