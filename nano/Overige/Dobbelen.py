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
            print(f"Je hebt {aantal} dobbelstenen gegooid. De resultaten zijn: {worpen}")
            print(f"Het totaal van die dobbelstenen is: {sum(worpen)}")
        else:
            print("Het aantal dobbelstenen moet positief zijn.")
    except ValueError:
        print("Voer alstublieft een numerieke waarde in.")