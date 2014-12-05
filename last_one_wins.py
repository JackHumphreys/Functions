import random

def n_counters():
    n_counters = int(input("Please enter the amount of counters you want within 10-50 inclusive: "))
    if n_counters < 10 and n_counters > 50:
        print("This amount is not valid. Try again.")
        n_counters = int(input("Please enter the amount of counters you want within 10-50 inclusive: "))
    else:
        return n_counters

def player_remove(counter):
    player_remove = int(input("Enter the amount of counter you wish to remove (1,2 or 3): "))
    while player_remove > 3 or player_remove < 1:
        print("This is not valid. Try again.")
        player_remove = int(input("Enter the amount of counter you wish to remove (1,2 or 3): "))
    counter = counter - player_remove
    if counter <= 0:
        print("You lose!")
    else:
        return counter
    
def comp_remove(counter):
    comp_remove = random.randint(1,3)
    print("Computer has removed {0}".format(comp_remove))
    counter = counter - comp_remove
    if counter <= 0:
        print("You lose!")
    else:
        return counter

counter = n_counters()
while counter >= 0:
    counter = player_remove(counter)
    comp_remove(counter)



