import time
from spel_onderdelen import clear_terminal as clear
from spel_onderdelen import Deler, Speler, maak_deck, bereken_waarde

deler = Deler()
speler = Speler()
clear()

while True:  # while loop
    """Main menu"""
    print("Welkom bij BlackJack\n1. Info\n2. Start\n3. Quit")
    spel = True  # spel is True
    if spel:  # als het True is
        keuze = input("Kies een nummer/letter: ").lower()  # input
        if keuze not in ["1", "2", "3", "i", "s", "q"]:  # niet in []
            clear()
            print("Ongeldige keuze!\n")
            continue

        match keuze:  # match keuze
            case "1" | "i":  # info
                clear()
                """Info van het spel"""
                print("Het doel van BlackJack is om een hand te krijgen zo dicht mogelijk bij 21 zonder eroverheen te gaan")
                print("Kaarten 2-10 tellen voor hun waarde, boer/vrouw/koning 10 punten, en een aas 1 of 11 punten")
                print("Speler kiest kaarten te nemen (Hit) of te stoppen (Stand)")
                print("dealer trekt tot minimaal 17, en degene met de hoogste waarde =<21 wint")
                input("\ndruk enige knop om terug te gaan:")
                clear()

            case "2" | "s":  # start het spel
                clear()
                deck = maak_deck()
                speler.hand.clear(); deler.hand.clear()
                deler.voeg_toe_kaart(deck.pop())
                speler.voeg_toe_kaart(deck.pop()); speler.voeg_toe_kaart(deck.pop())

                while True:  # waneer het True is
                    print(f"Deler hand: {', '.join(str(k) for k in deler.hand)}, ? ? (?)")
                    print("Deler waarde:", bereken_waarde(deler.hand))
                    print("\nSpeler hand:", ", ".join(str(k) for k in speler.hand))
                    print("Speler waarde:", bereken_waarde(speler.hand))
                    keuze = input("\nH/S ").lower()
                    if keuze not in ["h", "s"]:
                        clear()
                        print("ongeldige keuze!\n")
                    if keuze == "h":  # wanneer de speler hit
                        clear()
                        speler.voeg_toe_kaart(deck.pop())
                        if bereken_waarde(speler.hand) > 21:
                            spel = False
                            break
                    if keuze == "s":  # waaneer de speler stand
                        while bereken_waarde(deler.hand) < 17:
                            clear()
                            deler.voeg_toe_kaart(deck.pop())
                            print("Deler hand:", ", ".join(str(k) for k in deler.hand))
                            print("Deler waarde:", bereken_waarde(deler.hand))
                            time.sleep(1)
                        spel = False
                        break

            case "3" | "q":  # stopt het spel
                clear()
                print("Tot ziens!")
                break

    if not spel:  # als het False is
        clear()
        """Toont de kaarten en punten"""
        print("Deler hand:", ", ".join(str(k) for k in deler.hand))
        print("Deler waarde:", bereken_waarde(deler.hand))
        print("\nSpeler hand:", ", ".join(str(k) for k in speler.hand))
        print("Speler waarde:", bereken_waarde(speler.hand))

        """Checkt of de waardes gelijk zijn of groter of kleiner (:"""
        if bereken_waarde(speler.hand) == bereken_waarde(deler.hand):
            print("\nGelijk spel!")
        elif bereken_waarde(speler.hand) == 21:
            print("\nBlackjack! Speler wint!")
        elif bereken_waarde(speler.hand) > 21:
            print("\nPlayer bust! Dealer wint!")
        elif bereken_waarde(deler.hand) > 21:
            print("\nDealer bust! Speler wint!")
        elif bereken_waarde(speler.hand) > bereken_waarde(deler.hand):
            print("\nSpeler wint!")
        elif bereken_waarde(speler.hand) < bereken_waarde(deler.hand):
            print("\nDealer wint!")

        keuze = input("\nOpnieuw? Y/N ").lower()
        if keuze not in ["y", "n"]:
            clear()
            print("Ongeldige keuze!\n")
        match keuze:
            case "y":
                clear()
                continue
            case "n":
                print("Tot ziens!")
                break