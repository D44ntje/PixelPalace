def start_up():
    # Vraag de gebruiker om een keuze te maken
    welke_soort_eenheden = str.lower(input("Welke eenheden wil je omrekenen?\n1. Afstand.\n2. Gewicht.\n3. Temperatuur.\n4. Text naar morsecode.\n"))

    def eenheidskeuze():
       # afstand
       if welke_soort_eenheden == "afstand" or welke_soort_eenheden == "1":
           from nano.Overige.omreken import Afstand
           Afstand.start_up()
       # gewicht
       elif welke_soort_eenheden == "gewicht" or welke_soort_eenheden == "2":
           from nano.Overige.omreken import gewicht
           gewicht.start_up()
       # temperatuur
       elif welke_soort_eenheden == "temperatuur" or welke_soort_eenheden == "3":
           from nano.Overige.omreken import temperatuur
           temperatuur.start_up()
       # morsecode
       elif welke_soort_eenheden == "morsecode" or welke_soort_eenheden == "4":
           from nano.Overige.omreken import morsecode
           morsecode.start_up()
       # ongeldige invoer
       else:  # kiest een speler iets anders dan bovenstaande opties, dan zal hij opnieuw iets moeten invoeren
           print("\n\nJe hebt een ongeldige optie ingevoerd.\nControleer of u geen typfout heeft gemaakt.\n")
           eenheidskeuze()

    eenheidskeuze()
