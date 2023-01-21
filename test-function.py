def computepay(hours, rate): 
    if (hours > 40) : 
        print("Overtime!")
        overtime = int(hours) - 40
        overtime_pay = overtime * (1.5*10)
        total = overtime_pay + (40 * float(rate))
    else : 
        total = float(hours) * float(rate)
    return total


hours = input('Enter hours: ')
rate = input('Enter rate: ')
try:

    hours = int(hours)
    rate = float(rate)
except: 
    print("Error, please enter a numeric number!")
    quit()

print("Total pay: ", computepay(hours, rate))
