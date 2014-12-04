def fi_to_mc():
    foot = int(input("Please enter length in foot (round down): "))
    inches = int(input("Please enter remaining inches: "))
    metres = foot*0.3048
    cm = inches*2.54
    print("{0}foot {1}inches = {2}m {3}cm".format(foot,inches,metres,cm))

def mc_to_fi():
    metres = int(input("Please enter length in metres (round down): "))
    cm = int(input("Please enter remaining centimetres: "))
    foot = metres*3.2808399
    inches = cm*0.397
    print("{0}m {1}cm = {2}foot {3}inches".format(metres,cm,foot,inches))

choice = int(input("Type 0 for metre and centimetres to foot and inches. Type 1 for foot and inches to metres and centimetres. "))
if choice == 0:
    mc_to_fi()
elif choice == 1:
    fi_to_mc()
else:
    print("This is not defined.")

