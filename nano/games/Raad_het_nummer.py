import random
import math
from nano import colored_text
def start_game():
    print("Starting raad het nummer...")
    #vragen voor de grenzen van het spel
    lower = int(input("Kies een lage grens: "))
    upper = int(input("Kies een hoge grens: "))
    # een getal kiezen tussen de twee grenzen die de speler heeft gekozen
    x = random.randint(lower, upper)
    total_chances = math.ceil(math.log(upper - lower + 1, 2)) # gebruikt binary search om te bepalen hoeveel kansen er nodig zijn om het getal te raden
    count = 0 # dit houdt bij hoeveel rondes er al gespeeld zijn
    flag = False
    while count < total_chances:
        print("\n" * 1000)
        print(f"\n\t{colored_text.BLACK}{colored_text.BACKGROUND_BRIGHT_BLUE}Je hebt, {total_chances}, kansen om het getal te raden!{colored_text.RESET}")
        count += 1
        guess = int(input("\nKies een getal: ")) # vraagt de speler om een getal te kiezen
        if guess > upper or guess < lower: # zorgt ervoor dat de speler een getal kiest tussen zijn twee grenzen
            print(f"Je moet een getal tussen: {lower} en {upper} kiezen.")
            count -= 1
        if x == guess: # dit is voor als de speler het juist gokt
            print(f"Gefeliciteerd! je hebt het getal in,{count}, keer geraden")
            flag = True
            break
        elif lower < guess < x:
            print(f"{colored_text.BRIGHT_RED}Je gokte te laag!{colored_text.RESET}")
        elif upper > guess > x:
            print(f"{colored_text.BRIGHT_RED}Je gokte te hoog!{colored_text.RESET}")
    if not flag: # als het getal niet wordt geraden dan laat de computer zien welk getal het wel was
        print(f"\n\tHet getal was {colored_text.BRIGHT_BLUE}{x}{colored_text.RESET}")
        print(f"{colored_text.RED}\tVolgende keer beter!{colored_text.RESET}")
