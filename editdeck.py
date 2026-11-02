import os

def edit_deck():

    with open(f"decks/{name}.md" "r") as f:
        read = f.readlines()
        print(num)
        print()
        try:
            num = int(input("Please Enter The Number Of The Deck You Wish To Edit"))
        except:
            return "That Isn't A Valid Number"

        for line in num:
            if line.split("|")[0] == int(num):
                with open(f"decks/{read.split("|")[1]}.md" "w")
