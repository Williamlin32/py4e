
nlist = list()

while True:
    num = input('Enter a number: ')
    if num == "done": break
    nlist.append(num)
max = float(max(nlist))
min = float(min(nlist))

print("Maximum: ", max)
print("Minimum: ", min)
