import random
from nano import colored_text
def start_game():
    print("Starting Hangman...")
    # lijsten met woorden
    makkelijk = ['kat', 'boom', 'fiets', 'lamp', 'stoel', 'huis', 'plant', 'banaan', 'deur', 'vis', 'auto', 'boek', 'zon', 'pen', 'kop', 'bord', 'stoel', 'tent', 'regen', 'baan',
                 'jas', 'rok', 'pot', 'tas', 'klok', 'weg', 'riet', 'hek', 'weg', 'bus', 'maan', 'zoet', 'koek', 'muur', 'bal', 'gat', 'klap', 'doos', 'boom', 'bol',
                 'vis', 'kat', 'weg', 'bus', 'zon', 'schip', 'man', 'tak', 'paal']
    gemiddeld = ['trein', 'dokter', 'lantaarn', 'student', 'telefoon', 'zolder', 'brievenbus', 'museum', 'toetsenbord', 'keuken', 'fabriek', 'vrachtwagen', 'uitnodiging', 'wandelpad',
                 'huwelijk', 'spiegel', 'muziekstuk', 'kastanje', 'natuurkunde', 'toerisme', 'bibliotheek', 'hoofdstuk', 'december', 'instrument', 'medewerker', 'ontdekking',
                 'reclamebord', 'administratie', 'parachute', 'dierenarts', 'kookboek', 'schoonmaker', 'verjaardag', 'computermuis', 'netwerk', 'kraanvogel',
                 'televisie', 'klaslokaal', 'internationaal', 'knuffeldier', 'geheugen', 'verrekijker', 'formulering', 'koelkast', 'volleybal', 'afstandsbediening']
    moeilijk = ['encyclopedie', 'geometrie', 'psychologie', 'parallellogram', 'interdisciplinair', 'circumferentie', 'schilderkunst', 'oxymoron', 'audiovisueel', 'reproductie',
                'kwadratuur', 'hypothese', 'verantwoordelijkheid', 'transformatie', 'informatievoorziening', 'diplomatie', 'monochromatisch', 'democratisering',
                'onverschilligheid', 'retrospectief', 'proportionaliteit', 'uitgebreidheid', 'extraterritoriaal', 'verzelfstandiging', 'verbeeldingskracht', 'individueel',
                'synthese', 'associatief', 'morfologisch', 'intelligentie', 'verifieerbaarheid', 'onvergankelijkheid', 'abstractie', 'ethiek', 'beschouwing', 'filosofie',
                'fotodynamica', 'organisch', 'analytisch', 'calculatie', 'sociologie', 'grammaticaal', 'sceptisch', 'schilderachtig', 'contextueel', 'introspectie']

    # gebruiker kiest een niveau
    while True:
        niveau = input("Kies een niveau: 'makkelijk', 'gemiddeld', of 'moeilijk': ").lower()
        if niveau == 'makkelijk':
            woordenlijst = makkelijk
            break
        elif niveau == 'gemiddeld':
            woordenlijst = gemiddeld
            break
        elif niveau == 'moeilijk':
            woordenlijst = moeilijk
            break
        else:
            print("Ongeldige keuze.\nControleer of je geen spelfouten hebt gemaakt.")

    guessed_letters = []

    selected_item = random.choice(woordenlijst) # de computer kiest een woord
    total_chances = 6 # aantal kansen staat op 6, want [0, 1, 2, 3, 4, 5, 6] = 7 pogingen


    

    def check_win(): # checkt of de speler al heeft gewonnen
        for i in range(len(selected_item)): # dat doet hij door te kijken of elke letter van selected_item al in guessed_letters zit
            if selected_item[i] not in guessed_letters:
                return False
        return True

    def render_word(): # deze functie laat zien hoeveel letters in het woord zitten en welke letters al geraden zijn
        for a in range(len(selected_item)):
            if selected_item[a] in guessed_letters: # hier print de functie voor elke letter die wel in het woord zit de letter
                print(selected_item[a], '', end='')
            else:
                print('? ', end='') # hier print de functie voor elke character die nog niet is geraden een '?'
        print('')

    # deze functie print een deel van het poppetje
    def display_hangman(tries): # als deze functie wordt aangeroepen dan wordt het poppetje laten zien
        stages = [
            """
         --------
         |      |
         |      O
         |     \\|/
         |      |
         |     / \\
         -
         """ + colored_text.RED + """ You died... """ + colored_text.RESET + """
      """, # en tot slot zijn laatste leven
            """
         --------
         |      |
         |      O
         |     \\|/
         |      |
         |     / 
         -
         
      """, # hier zijn ena laatste leven
            """
         --------
         |      |
         |      O
         |     \\|/
         |      |
         |      
         -
         
      """, # hier zijn vijfde
            """
         --------
         |      |
         |      O
         |     \\|
         |      |
         |     
         -
         
      """, # hier de vierde
            """
         --------
         |      |
         |      O
         |      |
         |      |
         |     
         -
         
      """, # hier de derde
            """
         --------
         |      |
         |      O
         |    
         |      
         |     
         -
         
      """, # hier verliest de speler zijn tweede leven
            """
         --------
         |      |
         |      
         |       
         |      
         |     
         -
         
      """ # dit is de opbouw van de plek waar het poppetje wordt later wordt opgehangen, de speler verliest zijn eerste leven
        ]
        print(stages[tries])

    display_hangman(total_chances)
    render_word()

    while True:
        letter = input('Raad een letter of het woord: ') # vraagt om de gok van de speler

        if len(letter) == 1 and letter.isalpha():
            if letter in guessed_letters: # dit is voor als de ingevoerde letter al is geraden
                print("\n" * 10000)
                print('Die letter had je al geraden...')
            else:
                guessed_letters.append(letter)
                if letter in selected_item: # dit laat de speler weten of hij het goed heeft
                    print("\n" * 10000)
                    print(colored_text.BRIGHT_BLUE + 'Juist! ' + colored_text.RESET + 'Die zit in het woord.')
                    display_hangman(total_chances)
                    render_word()
                    if check_win(): # dit laat de speler weten of hij al alle letters heeft geraden
                        print('Je hebt gewonnen, want je hebt alle letters al geraden!')
                        print(f'Het woord was: {selected_item}')
                        break
                else: # als de speler het fout heeft zal er een leven van af gaan
                    print("\n" * 10000)
                    print(colored_text.BRIGHT_RED + 'Onjuist. ' + colored_text.RESET + 'Die zat er niet in...')
                    total_chances -= 1
                    display_hangman(total_chances)
                    render_word()


        elif len(letter) > 1: # dit is voor als de speler een woord wil raden
            if letter == selected_item:
                print('Je hebt het woord geraden!')
                break
            else:
                print("\n" * 10000)
                print('Onjuiste gok.')
                total_chances -= 1
                display_hangman(total_chances)
                render_word()
        else: # zorgt ervoor dat als de speler per ongeluk iets anders invult dan een letter dat er dan geen leven ervan af gaat.
            print("Je moet een letter of een woord raden.\n" + "Geen andere dingen!")
            total_chances += 1

        # kijkt of de speler nog levens over heeft
        if total_chances <= 0:
            print(f'Je hebt verloren! Het woord was: {selected_item}')
            break

        # dit laat zien hoeveel levens de speler nog heeft
        print(f'Je hebt nog {total_chances} levens over.')
        print(f"Deze letters heb je al geraden: {guessed_letters.sort()}\n")

    # vragen of de speler opnieuw wil spelen
    opnieuw = str.lower(input("Wil je nog een keer spelen?\n" + "'ja' of 'nee' "))
    if opnieuw == "ja":
        from nano.games import Hangman
        Hangman.start_game()
    else:
        print("Fijn dat je Hangman hebt gespeeld!")
