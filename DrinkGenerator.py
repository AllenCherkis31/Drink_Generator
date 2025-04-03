# Imports
import random
import re
import os



class DrinkGenerator:

    '''
    Function get_ingredients reads five text files and appends the contents of each into individual lists.
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
            


    # Select name from lists using random integers.
    def printName(w1,w3):
            
            print(DrinkGenerator.adjective[w1])
            print(DrinkGenerator.noun[w3])
        

    def printStuff(l1,b1,i1):

            print("Liquor: " + DrinkGenerator.liquor[l1])
            print("Bitters: " + DrinkGenerator.bitters[b1])
            print("Other: " + DrinkGenerator.extra[i1])
            
            
    # Print results to screen.         
    def generateDrink(self):

        name1 = DrinkGenerator.randName(self)
        name3 = DrinkGenerator.randNoun(self)
        drinkPrint = DrinkGenerator.randDrink(self)
        liq = DrinkGenerator.randLiq(self)
        bit = DrinkGenerator.randBit(self)
        ing = DrinkGenerator.randEx(self)

        # Clearing the Screen
        os.system('cls')


        print ("""

    And your drink is...
    __________________
    """)


        print ('\n')
        print ('\n')
        DrinkGenerator.printName(name1,name3)

        DrinkGenerator.printRandDrink(drinkPrint)

        print ('\n')
        print ('\n')

        print ("I N G R E D I E N T S")
        print ("_____________________")
        print ('\n')
        DrinkGenerator.printStuff(liq,bit,ing)

        

        

    # Print intro art.
    def printIntro(self):
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

    # Display game options.
    def gameOptions(self):

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
    def mainScreen(self):

        DrinkGenerator.printIntro(self)
        
        q = DrinkGenerator.sanitize_input(input("><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><"))
        
        while q != "":
            q = DrinkGenerator.sanitize_input(input("Press enter to play"))
                    
        option = 2

        DrinkGenerator.gameOptions(self)

        option = DrinkGenerator.sanitize_input(input(""))


        while option != '1' and option != '2' and option != '3':
            option = DrinkGenerator.sanitize_input(input("Input invalid. Please enter 1, 2, or 3."))


        if option == '1':
            DrinkGenerator.playGame(self)

        elif option == '2':
            DrinkGenerator.instructions(self)
            o = DrinkGenerator.sanitize_input(input("Press enter to return to main screen"))
            while o != "":
                o = DrinkGenerator.sanitize_input(input("Press enter to return to main screen"))
            DrinkGenerator.mainScreen(self)

        elif option == '3':
            print ("Bartender>  Why did you even show up in the first place?")
                        
            

        
    def instructions(self):
        print ("""

Bartender>  Welcome to the Drink Generator! Simply follow the on-screen instructions to create fantastic, unique drinks. Have fun and go f@#$ yourself!

        """)


        
    # Generates a drink and then either restarts or exits the program, depending on user action.
    def playGame(self):

            DrinkGenerator.generateDrink(self)

            pf = DrinkGenerator.sanitize_input(input("\nDo you want to try again? (y/n)"))

            while pf != 'y' and pf != 'n':
                pf = DrinkGenerator.sanitize_input(input("\nDo you want to try again? (y/n)"))
                
            if pf == 'y':
                DrinkGenerator.mainScreen(self)
            elif pf == 'n':
                print ("Bartender>  Here's your check.")


    # Functions which are responsible for generating random integers based on list length.
    def randName(self):
        w1 = random.randint(0,len(DrinkGenerator.adjective)-1)
        return w1

    def randNoun(self):

        w3 = random.randint(0,len(DrinkGenerator.noun)-1)
        return w3

    def randDrink(self):
        d1 = random.randint(1,3)
        return d1

    def randBit(self):
        b1 = random.randint(0,len(DrinkGenerator.bitters)-1)
        return b1

    def randLiq(self):
        l1 = random.randint(0,len(DrinkGenerator.liquor)-1)
        return l1

    def randEx(self):
        i1 = random.randint(0,len(DrinkGenerator.extra)-1)
        return i1
        
            
        
DrinkGenerator.mainScreen(0)







