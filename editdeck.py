
from fetch import *

def edit_deck():
    print(fetch_decks())
    request = input("Please Select The Name Of The Deck You Want To Edit: ")
    if request not in fetch_decks().split("\n"):
        return "We Could Not Find That Deck Name"

    with open(f"decks/{request}.md") as q:
        question = []
        for line in q.read().splitlines():
            question.append(line)
    print("\n".join(question))
    try:
        number = int(input("Please Enter The Number Of The Question You Want To Replace: "))
    except:
        return "Invalid Entry"
    full = []
    changed = False
    for entry in question:
        piece = entry.split("|")
        if int(piece[0]) != number:
            full.append(entry)
        else:
            changed = True
            full.append(f"{piece[0]}|{input("Please Enter The Question To Replace The Current Question: ")}|{input("Please Enter The Answer To That Question: ")}\n")
    if changed == True:
        with open(f"decks/{request}.md", "w") as y:
            y.write("\n".join(full))
    else:
        return "No Question With That Number Found"