# MasterMind_Python

<p>
the orgins of this game started as a simple pen and paper logic game called Bulls and Cows. 
but later evolved into a computer version called MOO. the more modern board game version was invented in 1970.
to pay homeage to this classic game i programmed it myself.
</p>

the principles i learned while coding are 
* working with loops
* classes
* expressions
* functions
* lists 
* user input
* variables


## how to play the game
<p>
The goal of this game is to guess the correct code.   
The game will start with the computer generating a random 4 letter code each letter representing a color.   
And then you will have a finite number of turns (the number depending on the difficulty you choose) to guess the correct combination.   
After you enter an answer the computer will tell you  
* how many of your answers were the correct color and in the correct position   
* how many of your answers were the correct color but not in the correct position  
*how many of your answers were completely incorrect  
With that knowledge you will be able to adjust your guess and try again  
The game ends when you run out of turns. Or you guess the right combination  
the colors you have at your disposal are b=blue r=red y=yellow g=green w=white  
as a note the computer is not programmed to generate a unique set of letters. So often-times a  
color may appear more then once in the answer.  
</p>

## program creation

i used the python extention in vs code

this program contains one class and 6 functions

* the one class is called Combo, which stores
a combination of four strings representing four 
colors

* game_setup generates and then returns
a Combo which it assigned random colors

* compare_combo takes in two Combos and prints out the details established in the rules of the game

* answer_checker determines whether the user input falls into the correct format for the game.

* main_loop asks the user for the information and states whether or not you won

* display_instructions prints the games instuctions for the user

* display displays the menu of options that allows the user to choose the look at instructions, look at game difficulty, or quit.


## how it works

the game starts with a menu option

![menu example](https://github.com/bshort95/MasterMind_Python/blob/master/Capture.JPG?raw=true)

when you enter 0 it will print the instuctions

![instructions example](https://github.com/bshort95/MasterMind_Python/blob/master/Capture1.JPG?raw=true)

when you choose your difficulty the game will start.

![starting example](https://github.com/bshort95/MasterMind_Python/blob/master/Capture2.JPG?raw=true)

the answer checker prevents you from entering the wrongly formatted enterees. 

![wrong number example](https://github.com/bshort95/MasterMind_Python/blob/master/Capture3.JPG?raw=true)

![wrong character example](https://github.com/bshort95/MasterMind_Python/blob/master/Capture4.JPG?raw=true)

when you guess you will be provided hints
![hint example](https://github.com/bshort95/MasterMind_Python/blob/master/Capture5.JPG?raw=true)

the games sends you back to main menu if you win
or run out of turns
![winning example](https://github.com/bshort95/MasterMind_Python/blob/master/Capture6.JPG?raw=true)
giving you the option to play again.


## bugs.

the compare_combo will seldom print out an incorrect number for 
the correct color but not in the correct spot. 

## useful websites
[Git](https://git-scm.com/)  
[visual studios code](https://code.visualstudio.com/)  
[Python](https://www.python.org/)  
[Python tutorials](https://www.w3schools.com/python)  
[Bulls and Cows](https://en.wikipedia.org/wiki/Bulls_and_Cows)


