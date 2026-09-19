# class genaamd Game
class Game:
    def __init__(self, naam, prijs): # lijst van Games en Prijzen
        self.naam = naam
        self.prijs = prijs

    def __str__(self):
        return f"{self.naam} - €{self.prijs:.2f}"

# class genaamd Wishlist
class Wishlist:
    def __init__(self):
        self.games = []  # lijst van Game-objecten

    def toon_spellen(self):
        if not self.games:
            print("Wishlist is leeg.")
        else:
            print("\n--- Jouw Wishlist ---")
            # for i, spel in enumerate(self.games, start=1):
            i = 0
            
            while i < len(self.games): 
                print(f"{i+1}. {self.games[i]}")
                i += 1

    def voeg_toe(self, game):
        self.games.append(game)

    def totaalprijs(self):
        totaal = sum(spel.prijs for spel in self.games)
        print(f"Totaalprijs van alle spellen: €{totaal:.2f}")


# Maak een wishlist-object
wishlist = Wishlist()

# Menu
while True:
    print("\n--- Wishlist Menu ---")
    print("1. Spellen bekijken")
    print("2. Spel toevoegen")
    print("3. Totaalprijs berekenen")
    print("4. Afsluiten")

# vraagt naar een getal
    keuze = input("Voer een getal in (1/2/3/4): ")

# als de gebruiker geen van de onderstaande getallen invoerd: error
    if keuze not in ["1", "2", "3", "4"]:
        print("Ongeldige keuze! Voer een getal in van 1 t/m 4.")
        continue

# matched de keuze met één van de cases
    match keuze:
        case "1":
            wishlist.toon_spellen()

        case "2":
            naam = input("Naam van het spel: ").strip()
            prijs = float(input("Prijs van het spel: "))
            wishlist.voeg_toe(Game(naam, prijs))
            print(f"{naam} is toegevoegd aan de wishlist")

        case "3":
            wishlist.totaalprijs()

        case "4":
            print("Programma stopt")
            break
