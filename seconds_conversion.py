def inputs():
    hours = int(input("Please enter hours: "))
    mins = int(input("Please enter minutes: "))
    secs = int(input("Please enter seconds: "))
    return hours,mins,secs

def seconds(secs):
    secs = secs
    return secs

def minutes(mins):
    secs = mins*60
    return secs

def hours(hours):
    mins = hours*60
    secs = mins*60
    return secs

def total_secs(seconds,minutes,hours):
    total = seconds+minutes+hours
    return total

def display_total(total_secs,hours,mins,secs):
    print("The total numbers of seconds of {0} hours, {1} minutes and {3} seconds is {4}

#Main Program
hours,mins,secs = inputs()
seconds = seconds(secs)
minutes = minutes(mins)
hours = hours(hours)
total_secs = total_secs(seconds,minutes,hours)


