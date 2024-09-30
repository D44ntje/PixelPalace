
def start_up():
    temperatuur_eenheden = {
        # algemene temperatuurschalen
        "C": "Celsius", "F": "Fahrenheit", "K": "Kelvin",
        # overige schalen
        "R": "Rankine", "Ré": "Réaumur",
    }
    conversiefactoren_temperatuur = {
        # Van Celsius naar andere schalen
        "C_to_F": lambda C: (C * 9 / 5) + 32,  # Celsius naar Fahrenheit
        "C_to_K": lambda C: C + 273.15,  # Celsius naar Kelvin
        "C_to_R": lambda C: (C + 273.15) * 9 / 5,  # Celsius naar Rankine
        "C_to_Re": lambda C: C * 4 / 5,  # Celsius naar Réaumur

        # Van Fahrenheit naar andere schalen
        "F_to_C": lambda F: (F - 32) * 5 / 9,  # Fahrenheit naar Celsius
        "F_to_K": lambda F: (F + 459.67) * 5 / 9,  # Fahrenheit naar Kelvin
        "F_to_R": lambda F: F + 459.67,  # Fahrenheit naar Rankine
        "F_to_Re": lambda F: (F - 32) * 4 / 9,  # Fahrenheit naar Réaumur

        # Van Kelvin naar andere schalen
        "K_to_C": lambda K: K - 273.15,  # Kelvin naar Celsius
        "K_to_F": lambda K: (K * 9 / 5) - 459.67,  # Kelvin naar Fahrenheit
        "K_to_R": lambda K: K * 9 / 5,  # Kelvin naar Rankine
        "K_to_Re": lambda K: (K - 273.15) * 4 / 5,  # Kelvin naar Réaumur

        # Van Rankine naar andere schalen
        "R_to_C": lambda R: (R - 491.67) * 5 / 9,  # Rankine naar Celsius
        "R_to_F": lambda R: R - 459.67,  # Rankine naar Fahrenheit
        "R_to_K": lambda R: R * 5 / 9,  # Rankine naar Kelvin
        "R_to_Re": lambda R: (R - 491.67) * 4 / 9,  # Rankine naar Réaumur

        # Van Réaumur naar andere schalen
        "Re_to_C": lambda Re: Re * 5 / 4,  # Réaumur naar Celsius
        "Re_to_F": lambda Re: (Re * 9 / 4) + 32,  # Réaumur naar Fahrenheit
        "Re_to_K": lambda Re: (Re * 5 / 4) + 273.15,  # Réaumur naar Kelvin
        "Re_to_R": lambda Re: (Re * 9 / 4) + 491.67  # Réaumur naar Rankine
    }

    print("""
    algemene temperatuurschalen:  | overige schalen:        |
    'C'   voor Celsius            | 'Ré'  voor Réaumur      |
    'F'   voor Fahrenheit         | 'R'   voor Rankine      |
    'K'   voor Kelvin             |                         |
    """
          )

    welke_eenheid_1 = input("\nWelke eenheden wil je verrekenen?" + "\nVan: ").upper()
    welke_eenheid_2 = input("Naar: ").upper()

    if welke_eenheid_1 in temperatuur_eenheden and welke_eenheid_2 in temperatuur_eenheden:
        try:
            def omrekenen():
                waarde = float(input(f"Hoeveel {temperatuur_eenheden[welke_eenheid_1]} wil je omrekenen: "))
                conversie_code = f"{welke_eenheid_1}_to_{welke_eenheid_2}"
                if conversie_code in conversiefactoren_temperatuur:
                    resultaat = conversiefactoren_temperatuur[conversie_code](waarde)
                    print(
                        f"{waarde} {temperatuur_eenheden[welke_eenheid_1]} is gelijk aan {resultaat} {temperatuur_eenheden[welke_eenheid_2]}")
                else:
                    print("Conversie tussen deze eenheden is niet beschikbaar.")


            omrekenen()

        except ValueError:
            print("Ongeldige invoer! Voer een numerieke waarde in.")
    else:
        print("De opgegeven eenheden zijn niet correct.")
