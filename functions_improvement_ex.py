# functions improvement exercise
# times-table tester
import random


def inputs():
    print("Times-table tester")
    print()
    testTable = int(input("Which times-table do you want to be tested on? "))
    return testTable

def questions(testTable):
    for questions in range(1,6):
        num1 = testTable
        num2 = random.randrange(2,13)
        ans = num1 * num2
        userAnswer = int(input(str(num1) + ' x ' + str(num2) + ' = ? '))
        if userAnswer == ans:
            print('Well done, you got the correct answer!')
            print()
        else:
            print('Sorry, you got the answer wrong. The correct answer is',ans)
            print()

def times_table_tester():
    testTable = inputs()
    questions(testTable)

# main program
times_table_tester()
              
