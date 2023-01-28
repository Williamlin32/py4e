fname = input("Enter file name: ")
try:
    fhand = open(fname)
except:
    print("File does not exist!")
    exit()

count = {}
for line in fhand:
    line.rstrip
    words = line.split()
    for word in words: 
        count[word] = count.get(word, 0) + 1

lst = list()
for key, val in count.items():
    newtemp = (val, key)
    lst.append(newtemp)

lst = sorted(lst, reverse=True)
for val, key in lst[:10]:
    print(key, val, "times")
