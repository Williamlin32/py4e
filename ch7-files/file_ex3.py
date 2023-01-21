fname = input("Enter the name of the file:")
try:
    fhand = open(fname)
except: 
    if fname == "na na boo boo":
        print("NA NA BOO BOO to YOU - You haven't been punk'd!")
        
    else: 
        print("File name cannot be opened:", fname)
    quit()

count = 0
for line in fhand:
    line = line.rstrip()
    if not line.startswith("Subject:"):
        continue
    count += 1

print("There were "+str(count)+" subject lines in", fname)