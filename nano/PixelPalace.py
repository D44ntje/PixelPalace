from nano.Overige.omreken import omrekenen
from nano.games import steen_papier_schaar
from nano.games import Raad_het_nummer
from nano.games import Word_scramble
from nano.games import Hangman
import Overige.Dobbelen
import colored_text

# welkomstbericht
name = input("Wat is jouw naam? ")
print(f"\n\t\t {colored_text.BOLD}{colored_text.BRIGHT_BLUE}{name}{colored_text.RESET}, welkom in: ") # speler wordt welkom geheten
print(colored_text.BRIGHT_BLUE + """  
         ooooooooo.   o8o                        ooooo  ooooooooo.            ooooo                                
        `888   `Y88.  `"'                        `888  `888   `Y88.           `888                                
         888   .d88' oooo  oooo    ooo  .ooooo.   888   888   .d88'  .oooo.    888   .oooo.    .ooooo.   .ooooo.  
         888ooo88P'  `888   `88b..8P'  d88' `88b  888   888ooo88P'  `P  )88b   888  `P  )88b  d88' `"Y8 d88' `88b 
         888          888     Y888'    888ooo888  888   888          .oP"888   888   .oP"888  888       888ooo888 
         888          888   .o8"'88b   888    .o  888   888         d8(  888   888  d8(  888  888   .o8 888    .o 
        o888o        o888o o88'   888o `Y8bod8P' o888o o888o        `Y888""8o o888o `Y888""8o `Y8bod8P' `Y8bod8P' 
""" + colored_text.RESET)

def speel_nog_iets():
    def keuzemenu_spelen():
        spelerskeuze = str.lower(input(
            "Wat wil je spelen?\n" + "1. Hangman.\n" + "2. Raad het nummer.\n" + "3. Rock, Paper, Scissors.\n" + "4. Word scramble.\n'terug'\n")) # vraagt de speler welk spel hij wil spelen
        if spelerskeuze == "1" or spelerskeuze == "hangman": # uitvoeren van optie 1
            print(f"\nJe hebt{colored_text.BRIGHT_BLUE} hangman{colored_text.RESET}, gekozen, succes!\n\n")
            Hangman.start_game()
        elif spelerskeuze == "2" or spelerskeuze == "raad het nummer":
            print(f"\nJe hebt{colored_text.BRIGHT_BLUE} raad het nummer{colored_text.RESET}, gekozen, succes!\n\n")
            Raad_het_nummer.start_game()
        elif spelerskeuze == "3" or spelerskeuze == "rock, paper, scissors":
            print(f"\nJe hebt{colored_text.BRIGHT_BLUE} rock paper scissors{colored_text.RESET}, gekozen, succes!\n\n")
            steen_papier_schaar.start_game()
        elif spelerskeuze == "4" or spelerskeuze == "word scramble":
            print(f"\nJe hebt{colored_text.BRIGHT_BLUE} word scramble{colored_text.RESET}, gekozen, succes!\n\n")
            Word_scramble.start_game()
        elif spelerskeuze == "terug":
            spelen_of_overig()
        else:
            print("\n\nJe hebt een ongeldige optie ingevoerd.\nControleer of u geen typfout heeft gemaakt.\n")
            keuzemenu_spelen()

    def keuzemenu_overig():
        gebruikerskeuze = str.lower(input("Wat wil je doen?\n1. Omrekenen.\n2. Dobbelen.\n'terug'\n"))
        if gebruikerskeuze == '1' or gebruikerskeuze == 'omrekenen':
            print(f"\nJe hebt{colored_text.BRIGHT_BLUE} omrekenen, {colored_text.RESET}gekozen, succes!")
            omrekenen.start_omrekenen()
        elif gebruikerskeuze == '2' or gebruikerskeuze == 'dobbelen':
            print(f"\nJe hebt{colored_text.BRIGHT_BLUE} dobbelen, {colored_text.RESET}gekozen, succes!")
            Overige.Dobbelen.start_up()
        elif gebruikerskeuze == 'terug':
            spelen_of_overig()

    def spelen_of_overig():
        spelen_of_iets_anders = str.lower(input("Kies een optie:\n1. spelen.\n2. Iets anders doen.\n"))
        if spelen_of_iets_anders == '1' or spelen_of_iets_anders == 'spelen':
            print("\n" * 1000)
            keuzemenu_spelen()
        elif spelen_of_iets_anders == '2' or spelen_of_iets_anders == 'iets anders':
            print("\n" * 1000)
            keuzemenu_overig()
        elif spelen_of_iets_anders == 'stop' or spelen_of_iets_anders == 'quit':
            print("")
        else:
            print("Ongeldige keuze. Probeer het opnieuw.")
            spelen_of_overig()
    spelen_of_overig()
    print("\n" * 1000)
    play_again = input("\nWil je nog wat anders doen??\n" + "Voer 'ja' of 'nee' in: ") # vragen aan de speler of hij nog iets wil spelen
    if play_again == "ja":
        print("Veel plezier bij je volgende game!\n")
        speel_nog_iets()
speel_nog_iets()
print(f"\nBedankt,{colored_text.BRIGHT_BLUE} {name}{colored_text.RESET} voor het spelen in PixelPalace!\nTot snel!")