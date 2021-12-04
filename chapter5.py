import time
import gameover

def chapter5_intro():
    print('this is chapter 5 intro')
    print("*" * 67)
    print()
    print()
    print()
    print()
    print('**Warn the cops about the killer around the house**')
    print('**Find the killer yourself**')
    print('**Leave the house**')

def Warn_the_cops_about_killer_hiding():
    move = False
    print('Player talk to the cop about killer hidden')
    print('Player trying to see whats coming next')
    print("And so on they finally found the killer and was arrested")
    time.sleep(3)
    while True:
        answer = input('Will you help them y/n')
        if answer == 'y':
            move = True
            break
        else:
            print('Mission Complete')
            time.sleep(3)
            return() #The player has won the game

def Find_the_killer_yourself():
    move = False
    print('Player walk in the basement')
    print('Player found the killer to catch him')
    print('Player was stabbed by the killer')
    time.sleep(3)
    gameover.gameover()

def Leave_the_house():
    move = False
    print('Player is leaving the house')
    print('Cops confront the Player but is still leaving')
    time.sleep(3)
    gameover.gameover()
