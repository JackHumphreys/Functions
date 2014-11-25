def inputs():
    hours_input = int(input("Please enter hours: "))
    mins = int(input("Please enter minutes: "))
    secs = int(input("Please enter seconds: "))
    return hours_input,mins,secs

def hours_mins_secs(hours_input,mins,secs):
    secs_secs = secs
    mins_secs = mins*60
    hours_secs = (hours_input*60)*60
    return secs_secs,mins_secs,hours_secs

def total_secs(seconds,minutes,hours):
    total = seconds+minutes+hours
    return total

def display_total(total,hours_input,mins,secs):
    print("The total numbers of seconds of {0} hours, {1} minutes and {2} seconds is {3} seconds.".format(hours_input,mins,secs,total))

def seconds_conversion():
    hours_input,mins,secs = inputs()
    seconds,minutes,hours = hours_mins_secs(hours_input,mins,secs) 
    total = total_secs(seconds,minutes,hours)
    display_total(total,hours_input,mins,secs)

seconds_conversion()
