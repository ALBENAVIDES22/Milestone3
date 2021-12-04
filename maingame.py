#Main module calls the ch1 function from chapter1 module
import chapter1


# Murder mystery game
def game_intro():
    #This game is about a detective solving a murder case of those couples and need to find who killed them
    print("*" * 67)
    print("**Play.Play_as_a_detective**")
    print("**Play.Play_the_beginning_of_the_mission**")
    print("**Play.take_place_from_sunny_day**")
    print("**Play.Walking_start**")

if __name__ == '__main__':
    print("*" * 67)
    print("**Intro.Game_is_starting**")
    print("**Intro.Choosing_difficulty**")
    print("**Intro.Cutscene_start**")
    print("**Intro.Game_pausing**")
    print("Before this game start, enter your name")
    playername = input("[Player Name: ]")
    game_intro()
    answer = input("\nWill you start this game(Y/N):")
    answer = answer.upper()
    if answer == 'Y':
        print("Calling the chapter 1 module\n")
        #while globalvariables.chap1finished != True: #create a chap1finished variable in globalvariables and initialize it to False
            #chapter1.ch1()
        chapter1.ch1()
        #while globalvariables.chap2finished != True:
            #chapter2.ch2()





