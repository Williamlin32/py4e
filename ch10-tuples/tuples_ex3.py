import string

fname = input("Enter a file name: ")
# try:
fhand = open(fname)
# except: 
#     print('File cannot be opened', fname)
#     exit()

for line in fhand:
    line.rstrip() #remove white space on right
    line.lower() #lower case
    line.translate(line.maketrans('','',string.punctuation)) #remove punctuation
    line.translate(line.maketrans('','', string.digits)) #remove digits
    line.replace(" ", "") #remove spaces 
    print(len(line))
