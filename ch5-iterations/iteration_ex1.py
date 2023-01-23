
sum = 0
count = 0 
while True: 
    
    num = input("Enter a number: ")
    if num == "done":
            print(sum, count, average)
            break 
    try:
        sum = sum + int(num) 
    except: 
        print("Invalid input")
        continue
    count += 1 
    average = float(sum) / count


