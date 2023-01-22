
count = {}

line = input("Enter a line of text: ")

words = line.split()

print('Words', words)
for word in words: 
    count[word] = count.get(word, 0) +1

print('Counts\n', count)