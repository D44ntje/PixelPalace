def start_omrekenen():
    while True:
        # Vraag de gebruiker om een keuze te maken
        welke_soort_eenheden = input("Welke eenheden wil je omrekenen?\n1. Afstand.\n2. Gewicht.\n3. Temperatuur.\n4. Text naar morsecode.\n").lower()

        # Afhandeling van de keuze
        if welke_soort_eenheden in ["afstand", "1"]:
            from nano.Overige.omreken import Afstand
            Afstand.start_up()
        elif welke_soort_eenheden in ["gewicht", "2"]:
            from nano.Overige.omreken import gewicht
            gewicht.start_up()
        elif welke_soort_eenheden in ["temperatuur", "3"]:
            from nano.Overige.omreken import temperatuur
            temperatuur.start_up()
        elif welke_soort_eenheden in ["morsecode", "4"]:
            from nano.Overige.omreken import morsecode
            morsecode.start_up()
        else:
            print("\n\nJe hebt een ongeldige optie ingevoerd.\nControleer of u geen typfout heeft gemaakt.\n")

        # Vraag de gebruiker of hij nog iets anders wil omrekenen
        while True:
            nog_iets = input("Wil je nog wat omrekenen?\nVoer 'ja' of 'nee' in: ").lower()
            if nog_iets == "nee":
                print("Dankjewel voor het gebruiken van de omreken machine!")
                return
            elif nog_iets == "ja":
                break
            else:
                print("Voer 'ja' of 'nee' in.")