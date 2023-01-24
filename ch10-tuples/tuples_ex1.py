
fname = input("Enter a file name: ")
fhand = open(fname)

count = {}
for line in fhand: 
    line.rstrip()
    if not line.startswith("From:"):
        continue
    words = line.split()
    count[words[1]] = count.get(words[1], 0) + 1


lst = []
for a, b in count.items():
    big = (b, a)
    lst.append(big)

lst.sort(reverse=True)
(value, key) = lst[0]
print(key, value)

