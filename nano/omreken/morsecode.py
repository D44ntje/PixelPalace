
def start_up():
    # Morsecode dictionary
    morse_code = {
        # Alfabet
        "A": ".-",       "B": "-...",     "C": "-.-.",    "D": "-..",     "E": ".",
        "F": "..-.",     "G": "--.",      "H": "....",    "I": "..",      "J": ".---",
        "K": "-.-",      "L": ".-..",     "M": "--",      "N": "-.",      "O": "---",
        "P": ".--.",     "Q": "--.-",     "R": ".-.",     "S": "...",     "T": "-",
        "U": "..-",      "V": "...-",     "W": ".--",     "X": "-..-",    "Y": "-.--",
        "Z": "--..",

        # Cijfers
        "0": "-----",    "1": ".----",    "2": "..---",   "3": "...--",   "4": "....-",
        "5": ".....",    "6": "-....",    "7": "--...",   "8": "---..",   "9": "----.",

        # Leestekens
        ".": ".-.-.-",   ",": "--..--",   "?": "..--..",  "'": ".----.",  "!": "-.-.--",
        "/": "-..-.",    "(": "-.--.",    ")": "-.--.-",  "&": ".-...",   ":": "---...",
        ";": "-.-.-.",   "=": "-...-",    "+": ".-.-.",   "-": "-....-",  "_": "..--.-",
        "\"": ".-..-.",  "$": "...-..-",  "@": ".--.-.",

        # Speciale tekens
        "SOS": "...---..."  # Internationale noodsignaal
    }

    # Omgekeerde mapping voor morse naar tekst
    morse_to_text = {v: k for k, v in morse_code.items()}

    def text_to_morse(text):
        """Converteert tekst naar morsecode."""
        return ' '.join(morse_code.get(char.upper(), '') for char in text)

    def morse_to_text_conversion(morse):
        """Converteert morsecode naar tekst."""
        return ''.join(morse_to_text.get(code, '') for code in morse.split(' '))

    # Gebruikersinvoer
    def gebruikersinvoer():
        keuze = input("Wil je tekst naar morsecode (T) of morsecode naar tekst (M) converteren? (T/M): ").upper()

        if keuze == 'T':
            tekst = input("Voer de tekst in die je wilt omzetten naar morsecode: ")
            resultaat = text_to_morse(tekst)
            print("\nMorsecode:", resultaat)
        elif keuze == 'M':
            morse = input("Voer de morsecode in die je wilt omzetten naar tekst: ")
            resultaat = morse_to_text_conversion(morse)
            print("\nTekst:", resultaat)
        else:
            print("\nOngeldige keuze! Kies T of M.")
            gebruikersinvoer()
    gebruikersinvoer()