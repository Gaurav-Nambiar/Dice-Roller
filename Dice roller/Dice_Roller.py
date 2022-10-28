import random

def printer_func(num = 0):
    if num == 1:
        print("\t-------")
        print("\t|     |")
        print("\t|  0  |")
        print("\t|     |")
        print("\t-------")    
    elif num == 2:
        print("\t-------")
        print("\t|0    |")
        print("\t|     |")
        print("\t|    0|")
        print("\t-------")
    elif num == 3:
        print("\t-------")
        print("\t|0    |")
        print("\t|  0  |")
        print("\t|    0|")
        print("\t-------")
    elif num == 4:
        print("\t-------")
        print("\t|0   0|")
        print("\t|     |")
        print("\t|0   0|")
        print("\t-------")
    elif num == 5:
        print("\t--------")
        print("\t|0   0|")
        print("\t|  0  |")
        print("\t|0   0|")
        print("\t--------")
    elif num == 6:
        print("\t-------")
        print("\t|0   0|")
        print("\t|0   0|")
        print("\t|0   0|")
        print("\t-------")

while True:
    print("\n\n\t1. Roll the dice  2. Exit\t")
    enter = int(input("\tEnter your option :"))
    if enter == 1:
        number=random.randint(1,6)
        printer_func(number)
    else:
        print("Thank you for using ''")
        break
