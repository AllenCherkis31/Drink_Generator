# Imports
import random
import re
import os

'''
The get_ingredients function reads five text files and appends the contents of each into individual lists.
These lists are stored within dictionary 'dict_of_lists'
'''


def get_ingredients(adjective_text_file, noun_text_file, bitters_text_file, liquor_text_file, extra_text_file):

    # List of text file names
    text_file_names = [adjective_text_file, noun_text_file, bitters_text_file, liquor_text_file, extra_text_file]

    # Empty dictionary which will store each list
    dict_of_lists = {}

    # For each file name
    for i in text_file_names:
        # Clear textfile_list
        textfile_list = []
        # Open/read file
        for word in open(i):
            # Remove newline characters
            textfile_list.append(word.rstrip('\n'))
        # Add textfile_list to dictionary
        dict_of_lists[text_file_names.index(i)] = textfile_list

    return dict_of_lists


# Call 'get_lists' function and provide five text file names
word_lists = get_ingredients('adjectives.txt', 'nouns.txt', 'bitters.txt', 'liquor.txt', 'extra.txt')

# Assign lists to respective variables.
adjective = word_lists[0]
noun = word_lists[1]
bitters = word_lists[2]
liquor = word_lists[3]
extra = word_lists[4]


def printRandDrink(d1):
    global randDrink


    if d1 == 1:
        print ('')
        print ('                /_O_\                ')
        print ('      __________| 0 |___________     ')
        print ('    /            \*/            \    ')
        print ('   |\            ***            /|   ') 
        print ('   | \____________*____________/ |   ') 
        print ('   | \                           |   ')
        print ('   |  \\\                         |   ')
        print ('   |    \\\                       |   ')
        print ('   |      \\\                     |   ')
        print ('   |        \\\                   |   ') 
        print ('   |\         \\\                 |   ') 
        print ('   | \\\         \\\               |   ')
        print ('   |   \\\         \\\             |   ')
        print ('   |     \\\         \\\           |   ') 
        print ('   |       \\\         \\\         |   ') 
        print ('   |         \\\         \\\       |   ')
        print ('   |           \\\         \\\     |   ')
        print ('   |             \\\         \\\   |   ')
        print ('   |               \\\         \\\ |   ')
        print ('   |                 \\\         \\|  ') 
        print ('   |                   \\\        |   ') 
        print ('   /_____________________\\\______\   ')

    if d1 == 2:
        print ('                                       ')
        print ('                             _-/_     ')
        print ('                            |{} |      ')
        print ('                            \___/      ') 
        print ('                            /         ') 
        print ('         __________________/__          ')
        print ('        \ \_______________/_/ /         ')
        print ('         \                   /          ')
        print ('          \ ############### /           ') 
        print ('           \ ############# /            ') 
        print ('            \ ########### /             ')
        print ('             \ ######### /              ')
        print ('              \ ####### /               ')
        print ('               \ ##### /                ')
        print ('                \ ### /                 ') 
        print ('                 \ # /                  ') 
        print ('                  \ /                    ')
        print ('                  | |                    ')
        print ('                  | |                    ') 
        print ('                  | |                    ') 
        print ('                  | |                    ')
        print ('                  | |                    ')
        print ('                  | |                    ')
        print ('                  | |                    ')
        print ('                  | |                    ') 
        print ('                  | |                  ') 
        print ('     _-_-_-_-_-_-_|_|_-_-_-_-_-_-_     ')

    if d1 == 3:

        print ('                                       ') 
        print ('       |\                       /|        ')
        print ('       ||#######################||         ')
        print ('       ||##############------###||         ') 
        print ('       ||#############|      |##||         ')
        print ('       ||#############|      |##||         ')
        print ('       ||##------#####|______|##||         ') 
        print ('       ||#|      |##############||         ')
        print ('       ||#|      |##############||         ')
        print ('       ||#|______|#######--#####||         ') 
        print ('       ||###############/^^\####||         ')
        print ('       ||################--#####||         ')
        print ('        -------------------------         ')
        



def printadjective(w1,w3):
        
        global adjective
        global noun

        print(adjective[w1])
        print(noun[w3])
    

def printStuff(l1,b1,i1):
        
        global bitters
        global liquor
        global extra

        print("Liquor: " + liquor[l1])
        print("Bitters: " + bitters[b1])
        print("Other: " + extra[i1])
        
        
        
def generateDrink():

    name1 = RandomNumber.randName()
    name3 = RandomNumber.randNoun()
    drinkPrint = RandomNumber.randDrink()
    liq = RandomNumber.randLiq()
    bit = RandomNumber.randBit()
    ing = RandomNumber.randEx()

    # Clearing the Screen
    os.system('cls')


    print ("""

And your drink is...
__________________
""")


    print ('\n')
    print ('\n')
    printadjective(name1,name3)

    printRandDrink(drinkPrint)

    print ('\n')
    print ('\n')

    print ("I N G R E D I E N T S")
    print ("_____________________")
    print ('\n')
    printStuff(liq,bit,ing)

    

    


def printIntro():
        # Clearing the Screen
        os.system('cls')

        print ('\n')
        print ('******************************************************************')
        print (')*****************************************************************(')
        print (')**|            ||                               ||            |**(')
        print (')**|            ||                               ||            |**(')
        print (')**|            ||                               ||            |**(')
        print (')**|            ||                               ||            |**(')
        print (')**|            /\                               /\            |**(')
        print (')**|           /()\                             /()\           |**(')
        print (')**|          / -- \                           / -- \          |**(')
        print (')**|                                                           |**(')
        print (')**|                                                           |**(')
        print (')**|                                                           |**(')
        print (')**|                                                           |**(')
        print ("""
                              _---_
                             /     \\     
                            |  ^ ^  |    
                            \\  c   /    
                             \\ .  /     
                             / -- \\  
                            /  >@< \\    
                           /        \\
                          /          \\                                           """)
        print ('        _________________/____________\_____________________       ')
        print ('       /  .      ,   |  |         .    _                ,   \       ')
        print ('      /     |##|     |__|             |?|   ,      \#/       \      ')
        print ('     / ,    |__|            ,       . |_|         . |         \     ')
        print ('    /_______________________________________________-__________\    ')
        print ('   |                                                           |    ')
        print ('   |                ------------------------                   |    ') 
        print ('   |                     D  R  I  N  K                         |    ')
        print ('   |                                                           |    ') 
        print ('   |                   G E N E R A T O R                       |    ') 
        print ('   |                 -----------------------                   |    ') 
        print ('   |                                                           |    ') 
        print ('   |                  PRESS ENTER TO START                     |    ')
        print ('   |                                                           |    ') 
        print ('   |                                                           |    ')
        print ('   ************************************************************    ')
        print ('\n')


def gameOptions():

    print ("_______________________________________")
    print ("|                                      |")
    print ("|     Welcome to Drink Generator       |")
    print ("|                                      |")
    print ("|        Enter \'1\' to begin            |")
    print ("|  Enter \'2\' to talk with bartender    |")
    print ("|         Enter \'3\' to quit            |")
    print ("|______________________________________|")



# Sanitizes user input.
def sanitize_input(input_string):
    # Allow alphanumeric characters and spaces
    sanitized = re.sub(r'[^a-zA-Z0-9\s]', '', input_string)
    return sanitized



# Prints intro and handles user input.                
def mainScreen():
    printIntro()
    
    q = sanitize_input(input("><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><"))
    
    while q != "":
        q = sanitize_input(input("Press enter to play"))
                
    option = 2

    gameOptions()

    option = sanitize_input(input(""))


    while option != '1' and option != '2' and option != '3':
        option = sanitize_input(input("Input invalid. Please enter 1, 2, or 3."))


    if option == '1':
        playGame()

    elif option == '2':
        instructions()
        o = sanitize_input(input("Press enter to return to main screen"))
        while o != "":
            o = sanitize_input(input("Press enter to return to main screen"))
        mainScreen()

    elif option == '3':
        print ("Don't let the door hit yer ass on the way out.")
                    
        

    
def instructions():
    print ("""

Welcome to the Drink Generator! Simply follow the on-screen instructions to
create fantastic, unique drinks. Have fun and go f@#$ yourself!

    """)


    
# Generates a drink and then either restarts or exits the program, depending on user action.
def playGame():

        generateDrink()

        pf = sanitize_input(input("\nDo you want to try again? (y/n)"))

        while pf != 'y' and pf != 'n':
            pf = sanitize_input(input("\nDo you want to try again? (y/n)"))
            
        if pf == 'y':
            mainScreen()
        elif pf == 'n':
            print ("Here's your check.")


# The RandomNumber class contains functions which are responsible for generating random integers based on list length.
class RandomNumber:
    def randName():
        w1 = random.randint(0,len(adjective)-1)
        return w1

    def randNoun():

        w3 = random.randint(0,len(noun)-1)
        return w3

    def randDrink():
        d1 = random.randint(1,3)
        return d1

    def randBit():
        b1 = random.randint(0,len(bitters)-1)
        return b1

    def randLiq():
        l1 = random.randint(0,len(liquor)-1)
        return l1

    def randEx():
        i1 = random.randint(0,len(extra)-1)
        return i1
        
            
        
mainScreen()







