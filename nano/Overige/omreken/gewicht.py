def start_up():
    # lijst met alle eenheden met keys
    eenheidsmogelijkheden = {
        # metrisch stelsel
        "mg": "milligram", "g": "gram", "kg": "kilogram", "t": "ton",
        # imperiaal/US stelsel
        "oz": "ounce", "lb": "pound", "st": "stone", "lt": "long ton", "sht": "short ton", "gr us": "grain US",
        # troy gewichtssysteem
        "oz t": "troy ounce", "lb t": "troy pound",
        # avoirdupois systeem
        "oz avdp": "avoirdupois ounce", "lb avdp": "avoirdupois pound",
        # apothekers systeem
        "scruple": "scruple", "dram": "dram", "gr": "grain",
        # astronomisch
        "M☉": "zonsmassa", "M⊕": "aardmassa",
        # japanse gewichtseenheden
        "kan": "kan", "monme": "monme",
        # chinese gewichtseenheden
        "jin": "jin", "liang": "liang",
        # historische gewichtseenheden
        "ct": "carat", "shekel": "shekel", "ducat": "ducat",
        # overige
        "slug": "slug", "amu": "atomic mass unit"
    }
    # conversiefactoren tussen verschillende eenheden, ten opzichte van 1 kilo
    conversiefactoren = {
        # Metrisch stelsel
        "mg": 0.001, "g": 1, "kg": 1000, "t": 1_000_000,
        # Imperiaal/US stelsel
        "oz": 28.3495, "lb": 453.592, "st": 6350.29, "lt": 1_016_047, "sht": 907_185, "gr us": 0.0647989,
        # Troy gewichtssysteem
        "oz t": 31.1035, "lb t": 373.242,
        # Avoirdupois systeem
        "oz avdp": 28.3495, "lb avdp": 453.592,
        # Apothekers systeem
        "scruple": 1.29598, "dram": 3.88794, "gr": 0.0647989,
        # Astronomisch
        "M☉": 1.989e30, "M⊕": 5.972e27,
        # Japanse gewichtseenheden
        "kan": 3750, "monme": 3.75,
        # Chinese gewichtseenheden
        "jin": 500, "liang": 50,
        # Historische gewichtseenheden
        "ct": 0.2, "shekel": 11.34, "ducat": 3.5,
        # Overige
        "slug": 14_593.9, "amu": 1.660539e-24
    }

    #mogelijkheden printen
    print( """
    metrisch stelsel:           | imperiaal/US stelsel:           | troy gewichtssysteem:   
    'mg'   voor milligram       | 'oz'    voor ounce              | 'oz t'   voor troy ounce
    'g'    voor gram            | 'lb'    voor pound              | 'lb t'   voor troy pound
    'kg'   voor kilogram        | 'st'    voor stone              |                           
    't'    voor ton             | 'lt'    voor long ton           |                           
                                | 'sht'   voor short ton          |                           
                                | 'gr us' voor grain US           |                           
    
    avoirdupois systeem:        | apothekers systeem:             | astronomisch:            
    'oz avdp' voor ounce        | 'scruple' voor scruple          | 'M☉'    voor zonsmassa   
    'lb avdp' voor pound        | 'dram'    voor dram             | 'M⊕'     voor aardmassa    
                                | 'gr ap'   voor grain apotheker  |                           
    
    japanse gewichtseenheden:   | chinese gewichtseenheden:       | historische gewichtseenheden:
    'kan'    voor kan           | 'jin'   voor jin                | 'ct'     voor carat
    'monme'  voor monme         | 'liang' voor liang              | 'shekel' voor shekel
                                                                  | 'ducat'  voor ducat
    
    overige:                    
    'slug'  voor slug           
    'amu'   voor atomic mass unit
    
        """
    )
    # vraag de gebruiker om welke eenheden het gaat
    welke_eenheid_1 = input("\nWelke eenheden wil je verrekenen?" + "\nVan: ").lower()
    welke_eenheid_2 = input("Naar: ").lower()

# controleer of de eenheden geldig zijn
    if welke_eenheid_1 in eenheidsmogelijkheden and welke_eenheid_2 in eenheidsmogelijkheden:
        try:
            def omrekenen():
                #vragen om hoeveel er omgerekend moet worden
                waarde = float(input(f"Hoeveel {eenheidsmogelijkheden[welke_eenheid_1]} wil je omrekenen?: "))

                # omrekenen naar meter
                waarde_in_gram = waarde * conversiefactoren[welke_eenheid_1]

                # omrekenen van meter naar de gewenste eenheid
                omgezette_waarde = waarde_in_gram / conversiefactoren[welke_eenheid_2]

                # print het resultaat
                print(f"{waarde} {eenheidsmogelijkheden[welke_eenheid_1]} is gelijk aan {omgezette_waarde:.4f} {eenheidsmogelijkheden[welke_eenheid_2]}")
            omrekenen()
        except ValueError:
            print("Ongeldige invoer. Voer een numerieke waarde in.")
            omrekenen()
    else:
        print("Een of beide eenheden zijn niet beschikbaar in de lijst.")
        start_up()

def replay():
     while True:
        nog_iets_anders = input("\nWil je nog andere eenheden omrekenen?\n'ja' of 'nee'? ").lower()
        if nog_iets_anders == 'ja':
            start_up()
        elif nog_iets_anders == 'nee':
            print("Okee, tot ziens!")
            break
        else:
            print("Ongeldige invoer. Typ 'ja' of 'nee'.")

if __name__ == "__main__":
    start_up()
    replay()
