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
    domain = words[1].split("@")
    count[domain[1]] = count.get(domain[1], 0)+1

print("Count:", count)