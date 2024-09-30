import random
def start_game():
    print("Starting word scramble...")
    makkelijk_woorden = [ "auto", "boot", "huis", "kat", "hond", "fiets", "bal", "boek", "pen", "lamp",
        "tafel", "stoel", "deur", "muur", "appel", "peer", "dorp", "stad", "weg", "trein",
        "jas", "boom", "voet", "hand", "broek", "schoen", "zon", "maan", "ster", "regen",
        "dak", "raam", "mes", "vork", "bord", "glas", "kop", "tent", "bed", "tuin",
        "vis", "vogel", "muur", "klok", "plant", "vloer", "rug", "kast", "neus", "oog" ] # niveau makkelijk
    normaal_woorden = [ "computer", "telefoon", "kantoor", "tandarts", "museum", "bibliotheek", "toerist", "dokter", "apotheek", "klaslokaal",
        "universiteit", "station", "vliegtuig", "wachtkamer", "gerecht", "politie", "ambtenaar", "onderwijzer", "presentatie", "project",
        "programmeren", "afspraak", "tentamen", "congres", "organisatie", "boekhouding", "fabriek", "website", "museum", "beheer",
        "ontwerp", "product", "dienst", "rekening", "resultaat", "vergadering", "investering", "rapport", "samenvatting", "analyse",
        "vergunning", "woning", "bewoner", "gemeente", "document", "formule", "oplossing", "beheerder", "verzekering", "bedrijf" ] # niveau normaal
    moeilijk_woorden = [ "filosofie", "psychologie", "geneeskunde", "archeologie", "cryptografie", "mathematiek", "quantumfysica", "linguïstiek", "astrofysica", "bacteriologie",
        "neurologie", "meteorologie", "jurisprudentie", "democratisering", "filantropie", "constitutie", "artificiële", "intelligentie", "biotechnologie", "nanotechnologie",
        "cyberbeveiliging", "semiotiek", "ontologie", "epistemologie", "bio-ethiek", "paleontologie", "sociolinguïstiek", "antropologie", "entomologie", "ecologie",
        "symbiose", "grammatica", "morfologie", "semantiek", "differentiatie", "integratie", "genetica", "evolutiebiologie", "telecommunicatie", "econometrie",
        "thermodynamica", "fotodynamica", "materialenwetenschap", "systematiek", "hydrodynamica", "verzilvering", "autoriteit", "procedure", "constructie", "classificatie" ] # niveau moeilijk

    foute_pogingen = [] # lijst met al geraden woorden

    moeilijkheidsgraad = str.lower(input("\nKies een niveau, 1, 2 of 3:\n" + "1. Makkelijk\n" + "2. Normaal\n" + "3. Moeilijk (expert)\n"))
    if moeilijkheidsgraad == "1" or moeilijkheidsgraad == "makkelijk": # woord kiezen uit de makkelijke lijst
        word = random.choice(makkelijk_woorden)
        shuffled = list(word)
        random.shuffle(shuffled)
        shuffled = ''.join(shuffled)
        count = 2
        flag = False # #
    elif moeilijkheidsgraad == "2" or moeilijkheidsgraad == "normaal": # woord kiezen uit de normale lijst
        word = random.choice(normaal_woorden)
        shuffled = list(word)
        random.shuffle(shuffled)
        shuffled = ''.join(shuffled)
        count = 5
        flag = False
    elif moeilijkheidsgraad == "3" or moeilijkheidsgraad == "moeilijk": # woord kiezen uit de moeilijke lijst
        word = random.choice(moeilijk_woorden)
        shuffled = list(word)
        random.shuffle(shuffled)
        shuffled = ''.join(shuffled)
        count = 10
        flag = False

    while count > 0:
        print(f"Je hebt {count} kansen.")
        count -= 1
        print("\n" + shuffled)

        gok = input("Om van niveau te veranderen typ: 'verander niveau'" + "\nRaad welk woord hier staat: ")
        try:
            int(gok)
            print("\n\nOngeldige invoer! Je mag geen numerieke waarde invoeren.")
            count += 1
            continue
        except ValueError:
            pass
        if gok == "verander niveau":
            import Word_scramble
            Word_scramble
        if gok == word:
            print("Gefeliciteerd, je hebt het woord geraden!")
            flag = True
            break

        if gok in foute_pogingen:
            print("Dit had je al geraden...")
            count += 1
        if gok != word:
            foute_pogingen.append(gok)
            print("Fout! Probeer opnieuw")
    if not flag:
        print("Je hebt het woord niet geraden!")
        print("Het woord was: " + word)
    opnieuw_spelen = input("Wil je nog een keer word scramble spelen?\n(Voer 'ja' of 'nee' in): ")
    if opnieuw_spelen == "ja":
        start_game()
    else:
        print("\nFijn dat je word scramble hebt gespeeld!")
