from random import choice

def start_spel():
    # kiest winnaar
    def kies_winnaar(spelers_keuze, computer_keuze):
        if spelers_keuze == computer_keuze:
            return "Gelijkspel!"
        elif spelers_keuze == "steen" and computer_keuze == "schaar":
            return "Je wint!"
        elif spelers_keuze == "papier" and computer_keuze == "steen":
            return "Je wint!"
        elif spelers_keuze == "schaar" and computer_keuze == "papier":
            return "Je wint!"
        else:
            return "De computer wint!"

    # tellers voor aantal potjes, wins en verliezen
    wins = 0
    spellen_gespeeld = 0
    verloren = 0

    keuzes = ["steen", "papier", "schaar"]

    print("Welkom bij Steen, Papier, Schaar!")
    print("Typ 'stop' om het spel te beëindigen.")

    while True:
        spelers_keuze = input("Kies steen, papier of schaar: ").lower()

        if spelers_keuze == 'stop':
            print("Bedankt voor het spelen!")
            print(f"Van de {spellen_gespeeld} spellen die je hebt gespeeld heb je er: {wins} gewonnen!\nEn {verloren} verloren.\nDat betekent dat je {spellen_gespeeld - wins - verloren} spellen gelijk hebt gespeeld.")
            break

        if spelers_keuze not in keuzes:
            print("Ongeldige keuze! Kies steen, papier of schaar.")
            continue

        computer_keuze = choice(keuzes)
        print(f"De computer kiest: {computer_keuze}")

        resultaat = kies_winnaar(spelers_keuze, computer_keuze)
        print(resultaat)

        spellen_gespeeld += 1

        if resultaat == 'Je wint!':
            wins += 1
        elif resultaat == 'De computer wint!':
            verloren += 1