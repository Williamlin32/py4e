fname = input("Enter the name of the file:")
try:
    fhand = open(fname)
except: 
    print("File name cannot be opened:", fname)
    quit()

count = {}

for line in fhand: 
    line.rstrip()
    if not line.startswith("From") or line.startswith("From:"): 
        continue
    words = line.split()
    count[words[2]] = count.get(words[2], 0)  + 1

print("Count: ", count)
