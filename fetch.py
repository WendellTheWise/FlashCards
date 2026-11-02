import os

def fetch_decks():
    decklist = []
    with open("decks/deck_list.md") as f:
        for line in f.read().splitlines():
            decklist.append(line)
    return "\n".join(decklist)

print(fetch_decks())