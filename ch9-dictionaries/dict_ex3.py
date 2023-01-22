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

print("Count: ", count)