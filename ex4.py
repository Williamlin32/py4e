
hours = input('Enter hours: ')
rate = input('Enter rate: ')

if (int(hours) > 40) : 
    print("Overtime!")
    overtime = int(hours) - 40
    overtime_pay = overtime * (1.5*10)
    total = overtime_pay + (40 * float(rate))
    print("Pay: ", total)
else : 
    total = float(hours) * float(rate)
    print("Pay: ", total)


