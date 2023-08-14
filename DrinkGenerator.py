


import random

#                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               here              
conName=['C H U N K Y','S M O O T H','P I S S E D - O F F','F U C K I N G','S C U M M Y','P O R T L Y','D A N K','T R A G I C','S A N D Y','S L U T T Y','P I N K','T H E  H U G E','M U S T Y','I N S T A G R A M  F A M O U S','R E F R E S H I N G','T A N G Y','B E W I L D E R E D','I T C H Y','M A S S I V E','P U R P L E','M U S H Y','S T A N K','N I C E','B L A C K','B L U E','W H I T E','E L','L I G H T','H E A V Y','D A R K','F R E N C H','K E N T U C K Y','T R I P L E','D O U B L E','S A S S Y','P R E T E N T I O U S']
#                                                                                                                                                                                                                                                                                                                                                                                                                                                           here 
nickname=['G O A T','O C E A N','P I C K L E','T I T T Y','A S S A S S I N','M O L E R A T','S T I N G R A Y','a n d  P R O U D','B E A N','W I Z A R D','L E M O N','B U C K S H O T','T A T E R  T O T','B E A C H','B I T C H','C O R N  W O R M','P R I N C E','M A S T A D O N','A R M P I T','S K I F F','S O U R','B O N G O','and H A I R Y','D I R T','R U S S I A N','L A D Y','S A I L O R','Z O M B I E','L A G O O N','S M A S H','T I C K L E  P A R T Y','C O W B O Y','P I R A T E','M O N K E Y','C H U N G U S']

bitters=['Orange','Angostura','Plum','Lavender','Peach','Apple Pie','Jelly Bean','Butterscotch']

liquor=['Bourbon','Rye','Vodka','Everclear','Moonshine','Tequila','Gin','Scotch']

extra=['Cherry','Orange Peel','Vanilla Bean','Lime','Lemon','Bacon','Cola','Ginger Beer','Milk','Someone put their cigar out in it','Mint']




def randName():
    w1 = random.randint(1,36)
    return w1



def randNickname():

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
        



def printConName(w1,w3):
        
        global conName
        global nickname

        
        if w1 == 1:
                print (conName[0])
        elif w1 == 2:
                print (conName[1])
        elif w1 == 3:
                print (conName[2])
        elif w1 == 4:
                print (conName[3])
        elif w1 == 5:
                print (conName[4])
        elif w1 == 6:
                print (conName[5])
        elif w1 == 7:
                print (conName[6])
        elif w1 == 8:
                print (conName[7])
        elif w1 == 9:
                print (conName[8])
        elif w1 == 10:
                print (conName[9])
        elif w1 == 11:
                print (conName[10])
        elif w1 == 12:
                print (conName[11])
        elif w1 == 13:
                print (conName[12])
        elif w1 == 14:
                print (conName[13])
        elif w1 == 15:
                print (conName[14])
        elif w1 == 16:
                print (conName[15])
        elif w1 == 17:
                print (conName[16])
        elif w1 == 18:
                print (conName[17])
        elif w1 == 19:
                print (conName[18])
        elif w1 == 20:
                print (conName[19])
        elif w1 == 21:
                print (conName[20])
        elif w1 == 22:
                print (conName[21])
        elif w1 == 23:
                print (conName[22])
        elif w1 == 24:
                print (conName[23])
        elif w1 == 25:
                print (conName[24])
        elif w1 == 26:
                print (conName[25])
        elif w1 == 27:
                print (conName[26])
        elif w1 == 28:
                print (conName[27])
        elif w1 == 29:
                print (conName[28])
        elif w1 == 30:
                print (conName[29])
        elif w1 == 31:
                print (conName[30])
        elif w1 == 32:
                print (conName[31])
        elif w1 == 33:
                print (conName[32])
        elif w1 == 34:
                print (conName[33])
        elif w1 == 35:
                print (conName[34])
        elif w1 == 36:
                print (conName[35])
                
        if w3 == 1:
                print (nickname[0])
        elif w3 == 2:
                print (nickname[1])
        elif w3 == 3:
                print (nickname[2])
        elif w3 == 4:
                print (nickname[3])
        elif w3 == 5:
                print (nickname[4])
        elif w3 == 6:
                print (nickname[5])
        elif w3 == 7:
                print (nickname[6])
        elif w3 == 8:
                print (nickname[7])
        elif w3 == 9:
                print (nickname[8])
        elif w3 == 10:
                print (nickname[9])
        elif w3 == 11:
                print (nickname[10])
        elif w3 == 12:
                print (nickname[11])
        elif w3 == 13:
                print (nickname[12])
        elif w3 == 14:
                print (nickname[13])
        elif w3 == 15:
                print (nickname[14])
        elif w3 == 16:
                print (nickname[15])
        elif w3 == 17:
                print (nickname[16])
        elif w3 == 18:
                print (nickname[17])
        elif w3 == 19:
                print (nickname[18])
        elif w3 == 20:
                print (nickname[19])
        elif w3 == 21:
                print (nickname[20])
        elif w3 == 22:
                print (nickname[21])
        elif w3 == 23:
                print (nickname[22])
        elif w3 == 24:
                print (nickname[23])
        elif w3 == 25:
                print (nickname[24])
        elif w3 == 26:
                print (nickname[25])
        elif w3 == 27:
                print (nickname[26])
        elif w3 == 28:
                print (nickname[27])
        elif w3 == 29:
                print (nickname[28])
        elif w3 == 30:
                print (nickname[29])
        elif w3 == 31:
                print (nickname[30])
        elif w3 == 32:
                print (nickname[31])
        elif w3 == 33:
                print (nickname[32])
        elif w3 == 34:
                print (nickname[33])
        elif w3 == 35:
                print (nickname[34])
                
                
#picks random nickname for user
def userNick(w4):
      
    if w4 == 1:
            return (nickname[0])
    elif w4 == 2:
            return (nickname[1])
    elif w4 == 3:
            return (nickname[2])
    elif w4 == 4:
            return (nickname[3])
    elif w4 == 5:
            return (nickname[4])
    elif w4 == 6:
            return (nickname[5])
    elif w4 == 7:
            return (nickname[6])
    elif w4 == 8:
            return (nickname[7])
    elif w4 == 9:
            return (nickname[8])
    elif w4 == 10:
            return (nickname[9])
    elif w4 == 11:
            return (nickname[10])
    elif w4 == 12:
            return (nickname[11])
    elif w4 == 13:
            return (nickname[12])
    elif w4 == 14:
            return (nickname[13])
    elif w4 == 15:
            return (nickname[14])
    elif w4 == 16:
            return (nickname[15])
    

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
    name3 = randNickname()
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
    printConName(name1,name3)

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







