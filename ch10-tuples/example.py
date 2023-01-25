import string
from collections import Counter

def letter_frequency(file_path):
    with open(file_path, 'r') as file:
        text = file.read().lower() # convert to lowercase
        text = text.translate(text.maketrans("", "", string.punctuation)) # remove punctuation
        text = text.translate(text.maketrans("", "", string.digits)) # remove digits
        text = text.replace(" ", "") # remove spaces
        letter_count = Counter(text)
        sorted_letter_count = sorted(letter_count.items(), key=lambda x: x[1], reverse=True)
        for letter, count in sorted_letter_count:
            print(letter, count)

letter_frequency("example.txt")