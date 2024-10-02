import random
def start_up():
    def gooi_dobbelstenen(aantal_dobbelstenen):
        resultaten = []
        for _ in range(aantal_dobbelstenen):
            worp = random.randint(1, 6)
            resultaten.append(worp)
        return resultaten

    # Vraag de gebruiker om het aantal dobbelstenen
    try:
        aantal = int(input("Hoeveel dobbelstenen wil je gooien? "))
        if aantal > 0:
            worpen = gooi_dobbelstenen(aantal)
            print(f"\nJe hebt {aantal} dobbelstenen gegooid. De resultaten zijn: {worpen}")
            print(f"Het totaal van die dobbelstenen is: {sum(worpen)}")
        else:
            print("Het aantal dobbelstenen moet positief zijn.")
    except ValueError:
        print("Voer alstublieft een numerieke waarde in.")
        start_up()
    def play_again():
        playagain = input("\nWil je nog een keer dobbelen?\n(Voer 'ja' of 'nee' in: ")
        if playagain.lower() == "ja":
            start_up()
        elif playagain.lower() == "nee":
            print("\nDankjewel voor het dobbelen!")
        else:
            play_again()
    play_again()
start_up()