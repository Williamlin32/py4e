
fname = input("Enter the name of the file:")
try:
    fhand = open(fname)
except: 
        print("File name cannot be opened:", fname)

for line in fhand: 
    line = line.upper()
    line = line.rstrip()
    print(line)