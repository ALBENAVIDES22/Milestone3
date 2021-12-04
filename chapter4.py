import time
import chapter5

def chapter4_intro():
    print('this is chapter 4 intro')
    print("*" * 67)
    print()
    print()
    print()
    print("**Go to the living room**")
    print("**Call the cops about the name you investigated**")

def Go_to_the_living_room():
    move = False
    print('Player checks the living room')
    print('Player going to the living room')
    print("Nothing there, is a nice room anyway")
    time.sleep(3)
    while True:
        answer = input("Will you contuine to stay y/n")
        if answer == 'n':
            break
        if answer == 'y':
            print('Stay to the living room')
            time.sleep(3)

def Call_the_cops_about_the_name_you_investigated():
    move = False
    print('Player found the victims name')
    print("Player is calling the cop for the investigation")
    print('Player ask the cop to come in the house')
    time.sleep(3)
    while True:
        answer = input("Will you continue searching the house y/n")
        if answer == 'y':
            move = True
            break
        else:
            print('You would try to find a killer')
            time.sleep(2)

    print('you will move to chapter 3')
    return move

def start():
    chapter4_intro()
    print('*' * 70)
    print('\nyou are calling chapter4\n')
    print('*' * 70)
    print("There are two options to do after you check the victims")
    print('1. Go to the living room')
    print('2. Call the cops about the name you investigated')
    option = input("which one do you like to do(1-2) or q for quit ")

    if option == '1':
        move = Go_to_the_living_room()
    if option == '2':
        move = Call_the_cops_about_the_name_you_investigated()

    if move == True:
        chapter5.start()
    else:
        print('Now you are exiting from this game')
    quit()

    # Chapter4finished = True
    # return Chapter4finished
