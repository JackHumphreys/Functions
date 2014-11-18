#Pay Calculations
#Jack Humphreys



def calculate_basic_pay(hours,pay):
    total = hours*pay
    return total

def calculate_overtime_pay(hours,pay):
    overtime_pay =(hours-40)*(pay*1.5)
    basic_pay = 40*pay
    total = overtime_pay + basic_pay
    return total

def calculate_total_pay(hours,pay):
    if pay <= 40:
        total = calculate_basic_pay(hours,pay)
    else:
        total = calculate_overtime_pay(hours,pay)
    return total

def work_details():
    hours = int(input("Please enter your hours: "))
    pay = float(input("Please your pay rate: "))
    return hours,pay

def calulate_pay(hours,pay):
    hours,pay = work_details()
    total = calculate_total_pay(hours,pay)

def display_total(total):
    print(total)

work_details()









    
