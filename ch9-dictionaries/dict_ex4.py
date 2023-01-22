fname = input("Enter the name of the file:")
try:
    fhand = open(fname)
except: 
    print("File name cannot be opened:", fname)
    quit()

count = {}
for lines in fhand:
    lines.rstrip()
    if not lines.startswith("From:"):
        continue
    words = lines.split()
    count[words[1]] = count.get(words[1], 0) +1

largest = None
key = None

for a,b in count.items():
    num = int(b)
    if largest is None or num > largest : 
        largest = num
        key = a

print(key, count[key])
