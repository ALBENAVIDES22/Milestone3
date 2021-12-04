import time
import Chapter2


#enter the couple home
def enter_house ():
    move = False
    print("option 2: task function is started...")
    print("*" * 67)
    print("**Go.Go_to_the_house**")
    print(("**Go.Enter_the_house**"))
    print("*" * 67)
    while True:
        answer = input("Will search the second floor")
        if answer == 'y':
            move = True
            break
        else:
            print('You can stay more in the first floor for searching')
            time.sleep(2)

    print('you will move to chapter 2')
    return move



#Chap1 Intro
def talk_cop():
    move = False
    print("Player is talking with a cop" )
    print("Now you have done it")
    time.sleep(2)
    while True:
        answer = input("Will you continue to stay y/n")
        if answer == 'n':
            move = True
            break
        if answer == 'y':
            print('Talk more')
            time.sleep(2)

    print('you will move to chapter 2')
    return move



def chap1_intro():
    print("Enter chapter 1 introduction")
    print("*" * 67)
    print()
    print()
    print()
    print("**Enter.Enter_outside_of_the_house**")
    print("**Enter.pick_up_the_knife (Y/N)**")
    print("**Enter.See_outside**")

def ch1():
    chap1_intro()
    print("There are two options you can find what's going on")
    print('1. talk to a cop')
    print('2. Enter the house')
    option = input("which one do you like to do(1-2) or q for quit ")
    if option == '1':
        move = talk_cop() #At the end of this function, player moves to chapter 2
    if option == '2':
        move = enter_house() #At the end of this function, player moves to chapter 2

    if move == True:
        Chapter2.start()
        #chap1finished = True
        #return chap1finished




