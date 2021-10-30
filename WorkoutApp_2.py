# Name: Sohaib Ahmed, @sohaibahmed7
# Date: October 29th, 2021
# Title: My Workout Application Project V2

# Importing Libraries
import time
from time import sleep


def plan(dayName):  # Does literally everything else
    file = open(dayName)
    lines = [line.strip("\n") for line in file if line != "\n"]
    for i in range(0, len(lines), 3):
        print("")
        print(lines[i])
        sets = int(lines[i+1])
        rest = int(lines[i+2])
        for i in range(sets):
            cont = input("Set #" + str(i+1) +
                         " Press ENTER when done (Enter Q to GO TO MENU). ")
            if (cont == "q") or (cont == "Q"):
                file.close()
                welcome()
            else:
                print(str(rest) + " seconds of rest.")
                sleep(rest)
                print("")
    file.close()


def welcome():  # Starting function
    print("1 = Push | 2 = Pull | 3 = Legs | Q = QUIT")
    start = input("What would you like to workout? ")
    if (start == "1"):
        plan("PushDay.txt")
    elif (start == "2"):
        plan("PullDay.txt")
    elif (start == "3"):
        plan("LegDay.txt")
    elif (start == "q") or (start == "Q"):
        print("damn u rlly leavin :'(")
        sleep(2)
        exit()
    else:
        print("Invalid input. Try again.")
        welcome()


welcome()
