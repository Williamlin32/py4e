
fname = input("Enter the name of the file: ")
try:
    fhand = open(fname)
except:
    print("File name cannot be opened:", fname)
    quit()

count = 0
for line in fhand:
    line = line.rstrip()
    count += 1 

print("The total number of lines is", count)