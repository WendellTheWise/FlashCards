import os

def create_deck(name):
    exitdeck = False
    if os.path.exists(f"decks/{name}.md"):
        return "This Deck Name Is Already Taken"
    else:
        with open("decks/deck_list.md", "a") as f:
            f.write(f"{name}")
        with open(f"decks/{name}.md", "a") as f:
            while exitdeck == False:
                question = input("Please Enter A Question To Enter Into The Deck Or Exit To Exit Deck Creator: ")
                if question.lower() == "exit":
                    exitdeck = True
                    continue
                answer = input("Please Enter The Answer To That Question: ")
                f.write(f"{len(f.readlines())}|{question}|{answer}\n")

