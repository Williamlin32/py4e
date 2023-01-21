
fname = input("Enter the name of the file:")
try:
    fhand = open(fname)
except: 
        print("File name cannot be opened:", fname)
        quit()

count = 0
num = 0
for line in fhand: 
    if not line.startswith('X-DSPAM-Confidence'):
        continue
    count += 1
    isp = line.find(':')
    num += float(line[isp+1:])

average = num / count
print("%.12f" % average)