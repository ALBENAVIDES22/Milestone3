import time
import chapter4

def chapter3_intro():
    print('This is chapter 3 intro')
    print("*" * 67)
    print()
    print()
    print()
    print("**Search the bloody hand prints**")
    print("**Check under the bed**")

def Search_the_bloody_handprints():
    move = False
    print('Player searching the hand prints of the victims')
    print("*" * 67)
    print("**Check the finger prints of who the victims are**")
    print("The name is revaled")
    print("*" * 67)
    while True:
        answer = input("Will you keep searching y/n")
        if answer == 'y':
            move = True
            break
        else:
            print('Call the cops about it')
            time.sleep(3)

    print('you will move to chapter 4')
    return move

def Checks_what_under_the_bed():
    move = False
    print('Player checks under the bed')
    print('Player sees a gun hiding under the bed')
    time.sleep(3)
    while True:
        answer = input ("Will you pick up the gun y/n")
        if answer == 'y':
            move = True
            break
        else:
            print('You can contiune searching the room')
            time.sleep(3)

    print('you will move to chapter 4')
    return move


def start():
    chapter3_intro()
    print('*' * 70)
    print('\nyou are calling chapter3\n')
    print('*' * 70)
    print("There are two options to look at the room")
    print('1. Search the bloody handprints')
    print('2. Check under the bed')
    option = input("which one do you like to do(1-2) or q for quit ")

    if option == '1':
        move = Search_the_bloody_handprints()
    if option == '2':
        move = Checks_what_under_the_bed()

    if move == True:
        chapter4.start()
        #chapter3finished = True
        #return chapter3finished