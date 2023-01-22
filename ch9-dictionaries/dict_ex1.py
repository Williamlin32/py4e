
handle = open("words.txt")

count = {}

while True:
    check = input("Enter the word you want to check: ")
    for lines in handle:
        words = lines.split()
        for word in words: 
            count[word] = None
    if check == "done":
        break
    elif check in count: 
        print("The word", check, "is in the file")
    else:
        print("The word", check, "is not in the file")

