from masterMind_combo import Combo
import random

##############################################
# game_setup generates and then returns
# a Combo which it assigned random colors
##############################################
def game_setup():
    s_colors = [" "," "," "," "]
    for x in range(0,4):
        rand = random.randrange(0,4)
        if rand == 0:
            s_colors[x] = "b"
        if rand == 1:
            s_colors[x] = "r"
        if rand == 2:
            s_colors[x] = "y"
        if rand == 3:
            s_colors[x] = "b"
        if rand == 4:
            s_colors[x] = "g"
    return Combo(s_colors[0],s_colors[1],s_colors[2],s_colors[3])


##############################################
# compare_combo takes in two Combos and prints 
# out the details established in the rules of 
# the game
##############################################
def compare_combo(combo1, combo2):
    list1 = combo1.show_colors()
    list2 = combo2.show_colors()    
    num_list = [0,0,0,0]
    same_color_bool = False
    same_spot = 0
    same_color = 0
    none_correct = 0

    for x in range(0,4):
        if list1[x] == list2[x]:
            same_spot = same_spot + 1
            num_list[x] = 1
                    
    for x in range(0,4):
        for y in range(0,4):
            if (num_list[y] != 1) and (num_list[x] != 1) and list1[x] == list2[y]:
                    num_list[y] = 1
                    same_color_bool = True
        
        if same_color_bool == True:
            same_color = same_color + 1      
            same_color_bool = False  
              
    none_correct = 4 - same_color - same_spot
    
    if(same_spot == 4):
        return True
    else:
        print(same_spot, "are correct")
        print(same_color, "are the right color wrong spot")
        print(none_correct, "are completly incorrect")
        return False 


##############################################
# answer_checker determines whether the user 
# input falls into the correct format for the game.
##############################################
def answer_checker(answer):
    answer.lower()
    answer_list = ["r","y","b","g","w"]
    letter_list = answer.split(" ")
    fs = True

    if len(letter_list) != 4:
        fs = True
        print("come on man. four entrees please. no more no less")
    elif (answer_list.count(letter_list[0]) == 0) or (answer_list.count(letter_list[1]) == 0) or (answer_list.count(letter_list[2]) == 0) or (answer_list.count(letter_list[3]) == 0):
        fs = True
        print("please only use the letters you are provided")   
    else:
        fs = False
    return fs


##############################################
# main_loop asks the user for the information 
# and states whether or not you won
##############################################
def main_loop(num):
    rival_combo = game_setup()
    print("please only enter the letters r, y, b, g, or w")
    print("please enter only four letters seperated by spaces")
    turn = 0
    win = False
    while turn < num:
        fs = True
        while fs:
            answer = input("enter letters here please: ")
            print(" ")
            fs = answer_checker(answer)
        letter_list = answer.split(" ")
        temp_combo = Combo(letter_list[0],letter_list[1],letter_list[2],letter_list[3])
        win = compare_combo(temp_combo,rival_combo)
        if win:
            print("congrats you guessed it right")
            print("you are the champion!")
            turn = num
        else:
            turn = turn + 1
            print("you have ", num - turn , "turns left")
            if turn == num:
                print("Game Over. the answer was")
                rival_combo.display()


##############################################
# display_instructions prints the games 
# instuctions for the user
##############################################
def display_instuction():
    print("The goal of this game is to guess the correct code.")
    print("The game will start with the computer generating a random") 
    print("4 letter code each letter representing a color.")
    print(" ") 
    print("And then you will have a finite number of turns (the number")
    print("depending on the difficulty you choose) to guess the correct")
    print("combination.")
    print(" ")
    print("After you enter an answer the computer will tell you")
    print("* how many of your answers were the correct color and in the correct position ")
    print("* how many of your answers were the correct color but not in the correct position")
    print("*how many of your answers were completely incorrect")
    print(" ")
    print("With that knowledge you will be able to adjust your guess and try again")
    print("The game ends when you run out of turns.") 
    print("Or you guess the right combination")
    print("")
    print("the colors you have at your disposal are") 
    print("b=blue r=red y=yellow g=green w=white")
    print("as a note, the computer is not programmed to generate") 
    print("a unique set of letters. So often-times a")
    print("color may appear more then once in the answer.")  


##############################################
# displays the menu of options that allows the 
# user to choose the look at instructions,
# look at game difficulty, or quit.
##############################################
def display():    
    option = 7
    exit = False
    print("welcome to a clasic logic game")
    while exit == False:
        print("---------------------------------------------")
        print("type the number 0 for instructions")
        print("type the number 1 for easy mode    (12 turns)")
        print("type the number 2 for regular mode (10 turns)")
        print("type the number 3 for hard mode    (8 turns)")
        print("type the number 4 for crazy mode   (4 turns)")
        print("type the number 5 to quit")
        print("---------------------------------------------")
    
    
        option = input("type here please: ")
        if option == "0":
            display_instuction()
        elif option == "1":
            main_loop(12)
        elif option == "2":
            main_loop(10)
        elif option == "3":
            main_loop(8)
        elif option == "4":
            main_loop(4)
        elif option == "5":
            exit = True
        else: 
            print("please enter a real option")

display()

















