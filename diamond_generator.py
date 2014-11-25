def inputs():
    odd_num = int(input("Please enter a odd number: "))
    if odd_num%2 == 0:
        print("This is an even number. Try again: ")
    else:
        odd_num = odd_num
    return odd_num

def diamond_generator(odd):
    star = ("*")
    middle = (star*odd)
    while star > 1:
        print(middle)
        print(middle-2)

odd = inputs()
diamond_generator(odd)
