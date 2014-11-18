hours = int(input("Please input hours you work: "))
rate = int(input("Please enter your hourly pay rate: "))
overtime = int(input("Please enter hours you worked overtime: "))
overtime_rate = int(input("Please input overtime pay rate: "))

print("Your basic pay is £{0}".format(hours*rate))
print("Your overtime pay is £{0}".format(overtime*overtime_rate))
print("Your total pay is £{0}".format((hour*rate)*(overtime*overtime_rate)))
           
