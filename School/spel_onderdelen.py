import random  # Nodig om het deck te shufflen
import os  # voor clear()


def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")


class Kaart:  # maakt de blauwdruk kaart aan om alle kaart gegevens op te slaan
    def __init__(self, symbool, naam, waarde):
        self.symbool = symbool
        self.naam = naam
        self.waarde = waarde

    def __str__(self):
        if isinstance(
            self.waarde, list  # de waarde zit in een lijst
        ):  # check of de waarde een lijst is (bijvoorbeeld [1,11])
            waarde_str = "/".join(
                map(str, self.waarde)
            )  # haalt de waardes 1,11 uit elkaar en maakt er met join een 1/11 van
        else:
            waarde_str = str(self.waarde)  # als het geen 1,11 bevat doe dit
        return f"{self.symbool} {self.naam} ({waarde_str})"  # alles mooi zetten


class Speler:  # blauwdruk voor de speler
    def __init__(self):
        self.hand = []  # de speler deck

    def voeg_toe_kaart(self, kaart):
        self.hand.append(kaart)  # Voegt een kaart toe aan speler.hand


class Deler:  # blauwdruk voor de deler
    def __init__(self):
        self.hand = []  # de deler deck

    def voeg_toe_kaart(self, kaart):
        self.hand.append(kaart)  # voegt een kaart toe aan de deler.hand


def maak_deck():
    symbolen = ["♠", "♥", "♦", "♣"]  # Alle 4 symbolen
    kaarten = [  # Alle mogelijke kaarten en hun waarden
        ("aas", [1, 11]),
        ("heer", [10]),
        ("dame", [10]),
        ("boer", [10]),
        ("10", [10]),
        ("9", [9]),
        ("8", [8]),
        ("7", [7]),
        ("6", [6]),
        ("5", [5]),
        ("4", [4]),
        ("3", [3]),
        ("2", [2]),
    ]
    deck = []  # het deck
    for symbool in symbolen:
        for naam, waarde in kaarten:
            deck.append(
                Kaart(symbool, naam, waarde)
            )  # voeg de kaart toe met de voorwaarden van class Kaart
    random.shuffle(deck)  # shuffle het deck voor prachtige resultaten (: (: (:
    return deck  # geeft het deck terug


def bereken_waarde(hand):  # functie om de waardes in de hand mee te berekenen
    totaal = 0  # totaal
    aantal_aas = 0  # aantal azen

    for kaart in hand:
        if isinstance(kaart.waarde, list):  # als waarde een lijst is
            if 11 in kaart.waarde:  # als 11 erin zit
                totaal += 11  # de aas wordt 11
                aantal_aas += 1  # 1 aas toegevoegd
            else:
                totaal += kaart.waarde[
                    0
                ]  # ik heb echt geen idee meer wat ik hier meer gedaan heb ): Demensia ): ): ):
        else:
            totaal += kaart.waarde  # anders is het totaal plus de kaart.waarde

    while (
        totaal > 21 and aantal_aas > 0
    ):  # als het totaal groter is dan 21 en aantal azen groter is dan 0
        totaal -= 10  # haal van de ene aas 10 eraf om de waarde van de aas 1 te geven
        aantal_aas -= 1  # haalt een aas weg
    return totaal  # geeft het totaal terug
