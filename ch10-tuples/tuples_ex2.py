
fname = input("Enter a file name: ")
fhand = open(fname)

count = {}
lst = []
for line in fhand: 
    line.rstrip()
    if not line.startswith("From") or line.startswith("From:"):
        continue
    words = line.split()
    time = words[5].split(":")
    count[time[0]] = count.get(time[0], 0) + 1

for a,b in count.items():
    hours = (a,b)
    lst.append(hours)

lst.sort()
for val, key in lst:
    print(val, key)
