import time
import chapter3


def Chapter2_intro():
    print('This is Chapter 2')
    print("*" * 67)
    print()
    print()
    print()
    print("**Walk.walk_upstairs_to_the_room**")
    print("**Go.Go_to_the_kitchen**")


#Dectitive walk into a couple room
#checking murder of the couple

def Go_upstairs_for_the_couple_room():
    move = False
    print('Player enters Go upstairs to the room function')
    print("*" * 67)
    print("**Walk.walk upstairs to the room**")
    print("Searching the bloody hand prints")
    print("*" * 67)
    while True:
        answer = input("Will search the couples room?")
        if answer == 'y':
            move = True
            break
        else:
            print('You can stay more in the first floor for searching')
            time.sleep(4)

    print('you will move to chapter 3')
    return move


def Go_kitchen():
    move = False
    print('Player enters Go Kitchen function')
    print("Player is going to the kitchen ")
    print("Nothing is there just a mess")
    time.sleep(3)
    while True:
        answer = input("Will you continue to stay y/n")
        if answer == 'n':
            break
        if answer == 'y':
            print('Stay to the kitchen')
            time.sleep(3)


# Call the function from chapter1
def start():
    Chapter2_intro()

    # Start option menu
    print('*' * 70)
    print('\nyou are calling chapter2\n')
    print('*' * 70)
    print("There are two options you can find what to look inside the house")
    print('1. Go upstairs to see a couples room')
    print('2. Go to the kitchen')
    option = input("which one do you like to do(1-2) or q for quit ")

    if option == '1':
        move = Go_upstairs_for_the_couple_room()
    if option == '2':
        move = Go_kitchen()

    if move == True:
        chapter3.start()
    # Added Codes
    else:
        print('Now you are exiting from this game')
    # terminate the game
    quit()

    # Chapter2finished = True
    # return Chapter2finished
