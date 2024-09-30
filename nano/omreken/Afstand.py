def start_up():
    # lijst met eenheden en hun volledige namen
    eenheidsmogelijkheden = {
        # Metrisch stelsel
        "mm": "millimeter", "cm": "centimeter", "dm": "decimeter", "m": "meter", "dam": "decameter", "hm": "hectometer",
        "km": "kilometer",
        # Imperiaal stelsel
        "in": "inch", "ft": "foot", "yd": "yard", "mi": "mile",
        # Zee en lucht
        "nm": "nautische mijl", "zm": "zeemijl"
    }

    # conversiefactoren tussen verschillende eenheden, allemaal ten opzichte van meter
    conversie_factoren = {
        # metrisch stelsel
        "mm": 0.001, "cm": 0.01, "dm": 0.1, "m": 1, "dam": 10, "hm": 100, "km": 1000,
        # imperiaal stelsel
        "in": 0.0254, "ft": 0.3048, "yd": 0.9144, "mi": 1609.34,
        # zee en lucht
        "nm": 1852, "zm": 1852  # 1 nautische mijl is hetzelfde als 1 zeemijl, maar beide benamingen kunnen gebruikt worden
    }
    print("""
    metrisch stelsel:           | imperiaal stelsel:             | zee en lucht:
    'mm'   voor millimeter      | 'in'   voor inch               | 'nm'  voor nautische mijl (zeemijl)
    'cm'   voor centimeter      | 'ft'   voor foot               |
    'dm'   voor decimeter       | 'yd'   voor yard               |
    'm'    voor meter           | 'mi'   voor mile               |
    'dam'  voor decameter       |                                |
    'hm'   voor hectometer      |                                |
    'km'   voor kilometer       |                                |
    """
    )
    # vraag de gebruiker om welke eenheden het gaat
    welke_eenheid_1 = input("Welke eenheden wil je verrekenen?\nVan: ").lower()
    welke_eenheid_2 = input("Naar: ").lower()


    # controleer of de eenheden geldig zijn
    if welke_eenheid_1 in eenheidsmogelijkheden and welke_eenheid_2 in eenheidsmogelijkheden:
        try:
            def omrekenen():
                #vragen om hoeveel er omgerekend moet worden
                waarde = float(input(f"Hoeveel {eenheidsmogelijkheden[welke_eenheid_1]} wil je omrekenen?: "))

                # omrekenen naar meter
                waarde_in_meter = waarde * conversie_factoren[welke_eenheid_1]

                # omrekenen van meter naar de gewenste eenheid
                omgezette_waarde = waarde_in_meter / conversie_factoren[welke_eenheid_2]

                # print het resultaat
                print(f"{waarde} {eenheidsmogelijkheden[welke_eenheid_1]} is gelijk aan {omgezette_waarde:.4f} {eenheidsmogelijkheden[welke_eenheid_2]}")

            omrekenen()
        except ValueError:
            print("Ongeldige invoer. Voer een numerieke waarde in.")
            omrekenen()
    else:
        print("Een of beide eenheden zijn niet beschikbaar in de lijst.")
        start_up()
def main():
    start_up()
    while True:
        nog_iets_anders = input("Wil je nog andere eenheden omrekenen?\n'ja' of 'nee'? ").lower()
        if nog_iets_anders == 'ja':
            start_up()
        elif nog_iets_anders == 'nee':
            print("Okee, tot ziens!")
            break
        else:
            print("Ongeldige invoer. Typ 'ja' of 'nee'.")
    main()