hours = int(input("Enter Hours: "))
rate = float(input("Enter Rate: "))

def computepay(hour, rate): 
    if hour > 40: 
        overpay = (hour - 40) * (rate * 1.5)
        total = (40 * rate) + overpay
    else: 
        total = hour * rate 
    print("Pay: ", total)

computepay(hours, rate)