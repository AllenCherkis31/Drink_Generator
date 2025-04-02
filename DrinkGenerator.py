# Imports
import random


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


def randName():
    w1 = random.randint(1,36)
    return w1

def randnoun():

    w3 = random.randint(1,35)
    return w3

def randDrink():
    d1 = random.randint(1,3)
    return d1

def randBit():
    b1 = random.randint(1,8)
    return b1

def randLiq():
    l1 = random.randint(1,8)
    return l1

def randIng():
    i1 = random.randint(1,11)
    return i1

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

        
        if w1 == 1:
                print (adjective[0])
        elif w1 == 2:
                print (adjective[1])
        elif w1 == 3:
                print (adjective[2])
        elif w1 == 4:
                print (adjective[3])
        elif w1 == 5:
                print (adjective[4])
        elif w1 == 6:
                print (adjective[5])
        elif w1 == 7:
                print (adjective[6])
        elif w1 == 8:
                print (adjective[7])
        elif w1 == 9:
                print (adjective[8])
        elif w1 == 10:
                print (adjective[9])
        elif w1 == 11:
                print (adjective[10])
        elif w1 == 12:
                print (adjective[11])
        elif w1 == 13:
                print (adjective[12])
        elif w1 == 14:
                print (adjective[13])
        elif w1 == 15:
                print (adjective[14])
        elif w1 == 16:
                print (adjective[15])
        elif w1 == 17:
                print (adjective[16])
        elif w1 == 18:
                print (adjective[17])
        elif w1 == 19:
                print (adjective[18])
        elif w1 == 20:
                print (adjective[19])
        elif w1 == 21:
                print (adjective[20])
        elif w1 == 22:
                print (adjective[21])
        elif w1 == 23:
                print (adjective[22])
        elif w1 == 24:
                print (adjective[23])
        elif w1 == 25:
                print (adjective[24])
        elif w1 == 26:
                print (adjective[25])
        elif w1 == 27:
                print (adjective[26])
        elif w1 == 28:
                print (adjective[27])
        elif w1 == 29:
                print (adjective[28])
        elif w1 == 30:
                print (adjective[29])
        elif w1 == 31:
                print (adjective[30])
        elif w1 == 32:
                print (adjective[31])
        elif w1 == 33:
                print (adjective[32])
        elif w1 == 34:
                print (adjective[33])
        elif w1 == 35:
                print (adjective[34])
        elif w1 == 36:
                print (adjective[35])
                
        if w3 == 1:
                print (noun[0])
        elif w3 == 2:
                print (noun[1])
        elif w3 == 3:
                print (noun[2])
        elif w3 == 4:
                print (noun[3])
        elif w3 == 5:
                print (noun[4])
        elif w3 == 6:
                print (noun[5])
        elif w3 == 7:
                print (noun[6])
        elif w3 == 8:
                print (noun[7])
        elif w3 == 9:
                print (noun[8])
        elif w3 == 10:
                print (noun[9])
        elif w3 == 11:
                print (noun[10])
        elif w3 == 12:
                print (noun[11])
        elif w3 == 13:
                print (noun[12])
        elif w3 == 14:
                print (noun[13])
        elif w3 == 15:
                print (noun[14])
        elif w3 == 16:
                print (noun[15])
        elif w3 == 17:
                print (noun[16])
        elif w3 == 18:
                print (noun[17])
        elif w3 == 19:
                print (noun[18])
        elif w3 == 20:
                print (noun[19])
        elif w3 == 21:
                print (noun[20])
        elif w3 == 22:
                print (noun[21])
        elif w3 == 23:
                print (noun[22])
        elif w3 == 24:
                print (noun[23])
        elif w3 == 25:
                print (noun[24])
        elif w3 == 26:
                print (noun[25])
        elif w3 == 27:
                print (noun[26])
        elif w3 == 28:
                print (noun[27])
        elif w3 == 29:
                print (noun[28])
        elif w3 == 30:
                print (noun[29])
        elif w3 == 31:
                print (noun[30])
        elif w3 == 32:
                print (noun[31])
        elif w3 == 33:
                print (noun[32])
        elif w3 == 34:
                print (noun[33])
        elif w3 == 35:
                print (noun[34])
                
                
#picks random noun for user
def userNick(w4):
      
    if w4 == 1:
            return (noun[0])
    elif w4 == 2:
            return (noun[1])
    elif w4 == 3:
            return (noun[2])
    elif w4 == 4:
            return (noun[3])
    elif w4 == 5:
            return (noun[4])
    elif w4 == 6:
            return (noun[5])
    elif w4 == 7:
            return (noun[6])
    elif w4 == 8:
            return (noun[7])
    elif w4 == 9:
            return (noun[8])
    elif w4 == 10:
            return (noun[9])
    elif w4 == 11:
            return (noun[10])
    elif w4 == 12:
            return (noun[11])
    elif w4 == 13:
            return (noun[12])
    elif w4 == 14:
            return (noun[13])
    elif w4 == 15:
            return (noun[14])
    elif w4 == 16:
            return (noun[15])
    

def theBit(b1):
      
    if b1 == 1:
            return (bitters[0])
    elif b1 == 2:
            return (bitters[1])
    elif b1 == 3:
            return (bitters[2])
    elif b1 == 4:
            return (bitters[3])
    elif b1 == 5:
            return (bitters[4])
    elif b1 == 6:
            return (bitters[5])
    elif b1 == 7:
            return (bitters[6])
    elif b1 == 8:
            return (bitters[7])

def theLiq(l1):
      
    if l1 == 1:
            return (liquor[0])
    elif l1 == 2:
            return (liquor[1])
    elif l1 == 3:
            return (liquor[2])
    elif l1 == 4:
            return (liquor[3])
    elif l1 == 5:
            return (liquor[4])
    elif l1 == 6:
            return (liquor[5])
    elif l1 == 7:
            return (liquor[6])
    elif l1 == 8:
            return (liquor[7])

def theIng(i1):
      
    if i1 == 1:
            return (extra[0])
    elif i1 == 2:
            return (extra[1])
    elif i1 == 3:
            return (extra[2])
    elif i1 == 4:
            return (extra[3])
    elif i1 == 5:
            return (extra[4])
    elif i1 == 6:
            return (extra[5])
    elif i1 == 7:
            return (extra[6])
    elif i1 == 8:
            return (extra[7])
    elif i1 == 9:
            return (extra[8])
    elif i1 == 10:
            return (extra[9])
    elif i1 == 11:
            return (extra[10])

def printStuff(l1,b1,i1):
        
        global bitters
        global liquor
        global extra

        
        
        
        if l1 == 1:
                print ("Liquor: "+liquor[0])
        elif l1 == 2:
                print ("Liquor: "+liquor[1])
        elif l1 == 3:
                print ("Liquor: "+liquor[2])
        elif l1 == 4:
                print ("Liquor: "+liquor[3])
        elif l1 == 5:
                print ("Liquor: "+liquor[4])
        elif l1 == 6:
                print ("Liquor: "+liquor[5])
        elif l1 == 7:
                print ("Liquor: "+liquor[6])
        elif l1 == 8:
                print ("Liquor: "+liquor[7])
            

        if b1 == 1:
                print ("Bitters: "+bitters[0])
        elif b1 == 2:
                print ("Bitters: "+bitters[1])
        elif b1 == 3:
                print ("Bitters: "+bitters[2])
        elif b1 == 4:
                print ("Bitters: "+bitters[3])
        elif b1 == 5:
                print ("Bitters: "+bitters[4])
        elif b1 == 6:
                print ("Bitters: "+bitters[5])
        elif b1 == 7:
                print ("Bitters: "+bitters[6])
        elif b1 == 8:
                print ("Bitters: "+bitters[7])

        if i1 == 1:
                print ("Other: "+extra[0])
        elif i1 == 2:
                print ("Other: "+extra[1])
        elif i1 == 3:
                print ("Other: "+extra[2])
        elif i1 == 4:
                print ("Other: "+extra[3])
        elif i1 == 5:
                print ("Other: "+extra[4])
        elif i1 == 6:
                print ("Other: "+extra[5])
        elif i1 == 7:
                print ("Other: "+extra[6])
        elif i1 == 8:
                print ("Other: "+extra[7])
        elif i1 == 9:
                print ("Other: "+extra[8])
        elif i1 == 10:
                print ("Other: "+extra[9])
        elif i1 == 11:
                print ("Other: "+extra[10])
        
def nameComputer():

    name1 = randName()
    name3 = randnoun()
    drinkPrint = randDrink()
    liq = randLiq()
    bit = randBit()
    ing = randIng()


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


class Main:

    def __init__(self, start, option):
        self.start = start
        self.option = option


                
def mainScreen():
    printIntro()
    
    q = input("><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><")

    while q != "":
        q = input("Press enter to play")
                
    option = 2

    gameOptions()

    option = input("")


    while option != '1' and option != '2' and option != '3':
        option = input("Input invalid. Please enter 1, 2, or 3.")


    if option == '1':
        playGame()

    elif option == '2':
        instructions()
        o = input("Press enter to return to main screen")
        while o != "":
            o = input("Press enter to return to main screen")
        mainScreen()

    elif option == '3':
        print ("Don't let the door hit yer ass on the way out.")
                    
        

    
def instructions():
    print ("""

Welcome to the Drink Generator! Simply follow the on-screen instructions to
create fantastic, unique drinks. Have fun and go fuck yourself!

    """)


    

def playGame():



        nameComputer()

        

        pf = input("\nDo you want to try again? (y/n)")

        while pf != 'y' and pf != 'n':
            pf = input("\nDo you want to try again? (y/n)")
            
        if pf == 'y':
            mainScreen()
        elif pf == 'n':
            print ("Here's your check.")
        
            


                   
            

                
            
            
        
        

        
mainScreen()

#recursion calls function rather than adding to it (iteration)







