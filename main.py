import random
import os
from fetch import *
from makedeck import *
number = True
exit = False
while exit == False:
    os.system('clear')
    print("""Welcome To Flash Card Central

    1: Quiz Yourself On A Flash Card Deck
    2: Create A New Flash Card Deck
    3: Manage An Existing Flash Card Deck
    4: Delete A Flash Card Deck
    5: Exit
    """)
    request = input("Please Select An Option By Entering The Associated Number: ")
    try:
        int(request)
    except:
        number = False

    elif number == True and request == 1:
        os.system('clear')
        print(fetch_decks())
        deck = input("Which Deck Would You Like To Quiz On? ")
        quiz(deck)
        os.system('clear')

    elif number == True and request == 2:
        os.system('clear')
        deck = input("What Will Be The Name Of This Deck? ")
        create_deck(deck)
        os.system('clear')

    elif number == True and request == 3:
        os.system('clear')
        edit_deck()

    elif number == True and request == 4:
        os.system('clear')
        print(fetch_decks())
        deck = input("Which Deck Would You Like To Delete? ")
        remove_deck(deck)
        os.system('clear')
    
    elif number == True and request == 5:
        exit = True
    
    else:
        print("Sorry, That Is Not An Availiable Option. Please Enter A Valid Number")
        print()
        input("Press Enter To Continue")