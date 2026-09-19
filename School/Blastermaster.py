import mysql.connector, os
from tabulate import tabulate  # Hiermee kunnen we nette tabellen maken

# Functie om het scherm leeg te maken
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Verbind met de MySQL-database
def connect_db():
    return mysql.connector.connect(
        host="localhost", 
        user="sukkel", 
        password="sukkel", 
        database="mydatabase"
    )

# Start verbinding en cursor
db = connect_db()
mycursor = db.cursor(dictionary=True)  # dictionary=True zorgt dat we kolomnamen kunnen gebruiken

try:
    while True:  # Main loop
        # Instructie
        print("\nWelkom player bij arcade Blastermasters")
        print("\n---Instructies---")
        print("Wil je alleen bekijken, dan skip je de 3 hieronder!")
        print("--Voeg eerst de game toe als je een nieuwe game hebt")
        print("--Voeg daarna je speler in")
        print("--En dan je highscore. Als je die hebt!!!")

        # Hoofdmenu
        print("\n---Opties---")
        print("1. Game toevoegen")
        print("2. Speler toevoegen")
        print("3. Highscore toevoegen")
        print("4. Alle spellen bekijken")
        print("5. Alle spelers bekijken")
        print("6. Game highscores bekijken")
        print("7. Player highscores bekijken")
        print("8. Winst bekijken per spel")

        keuze = input("\nKies een nummer: ")

        # Controle of de keuze geldig is
        if keuze not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
            print("ERROR: ongeldig nummer!")
            continue

        match keuze:
            # -------------------- CASE 1 --------------------
            case "1":
                clear()
                # Laat bestaande games zien
                mycursor.execute("SELECT * FROM game")
                myresult = mycursor.fetchall()

                # Zet alles netjes in een tabel
                table = [
                    (
                        str(y["game_id"]),
                        y["spelnaam"],
                        y["genre"],
                        f"€{float(y['prijs']):.2f}",
                    )
                    for y in myresult
                ]
                print(
                    tabulate(
                        table,
                        headers=["ID", "Spelnaam", "Genre", "Prijs"],
                        tablefmt="grid",
                        stralign="left",
                    )
                )

                # Gebruiker vult gegevens in
                spelnaam = input("NAAM: ")
                genre1 = input("GENRE 1: ")
                print("---Optioneel---")
                genre2 = input("GENRE 2: ")

                # Als er geen tweede genre is, wordt de prijs lager
                if genre2 == "":
                    genre = f"{genre1}"
                    prijs = 1.00
                else:
                    genre = f"{genre1} / {genre2}"
                    prijs = 1.50

                # Voeg de game toe aan database
                game_gegevens = "INSERT INTO game (spelnaam, genre, prijs) VALUES (%s, %s, %s)"
                val_game = (spelnaam, genre, prijs)
                mycursor.execute(game_gegevens, val_game)
                db.commit()
                print("\nGelukt: alles is toegevoegd!")

                # Laat de toegevoegde game zien
                return_game = mycursor.lastrowid
                mycursor.execute("SELECT * FROM game WHERE game_id = %s", (return_game,))
                myresult = mycursor.fetchall()

                table = [
                    (
                        str(y["game_id"]),
                        y["spelnaam"],
                        y["genre"],
                        f"€{float(y['prijs']):.2f}"
                    )
                    for y in myresult
                ]
                print(
                    tabulate(
                        table,
                        headers=["ID", "Naam", "Genre", "Prijs"],
                        tablefmt="grid",
                        stralign="left",
                    )
                )

            # -------------------- CASE 2 --------------------
            case "2":
                clear()
                # Nieuwe speler aanmaken
                player_naam = input("SPELER NAAM: ")
                player_email = player_naam + "@blasmaster.nova"  # Automatisch e-mailadres maken (:

                # Speler toevoegen aan database
                player_gegevens = "INSERT INTO player (player_naam, player_email) VALUES (%s, %s)"
                val_player = (player_naam, player_email)
                mycursor.execute(player_gegevens, val_player)
                db.commit()
                print("\nGelukt: alles is toegevoegd!")

                # Laat de nieuwe speler zien
                return_player = mycursor.lastrowid
                mycursor.execute("SELECT * FROM player WHERE player_id = %s", (return_player,))
                myresult = mycursor.fetchall()

                table = [
                    (str(x["player_id"]),
                     x["player_naam"],
                     x["player_email"]
                    )
                    for x in myresult
                ]
                print(
                    tabulate(
                        table,
                        headers=["ID", "Naam", "Email"],
                        tablefmt="grid",
                        stralign="left",
                    )
                )

            # -------------------- CASE 3 --------------------
            case "3":
                clear()
                # Laat eerst alle games zien zodat de gebruiker kan kiezen
                mycursor.execute("SELECT * FROM game")
                myresult = mycursor.fetchall()

                table = [
                    (
                        str(f["game_id"]),
                        f["spelnaam"],
                        f["genre"],
                        f"€{float(f['prijs']):.2f}",
                    )
                    for f in myresult
                ]
                print(
                    tabulate(
                        table,
                        headers=["ID", "Spelnaam", "Genre", "Prijs"],
                        tablefmt="grid",
                        stralign="left",
                    )
                )

                # Speler zoeken op naam
                player_id_highscore = input("PLAYER NAAM: ")
                mycursor.execute("SELECT player_naam, player_id FROM player WHERE player_naam = %s",(player_id_highscore,),)
                result = mycursor.fetchone()

                # Controleer of de gekozen speler bestaat
                if result is None:
                    print("ERROR: PLAYER_NAAM staat niet in de lijst")
                    continue

                print(f"SPELER GEVONDEN: {result['player_naam']} (ID: {result['player_id']})")

                # Controleer of de gekozen game bestaat
                game_id_highscore = input("GAME ID: ")
                mycursor.execute("SELECT game_id FROM game WHERE game_id = %s", (game_id_highscore,))
                result1 = mycursor.fetchone()

                if result1 is None:
                    print("ERROR: GAME ID staat niet in de lijst! Kies een GAME ID uit de lijst.")
                    continue

                # Highscore-gegevens vragen
                pogingen = input("POGINGEN: ")
                high_score = input("HIGHSCORE: ")
                print("\nVOORBEELD: DD-MM-YYYY")
                highscore_datum = input("DATUM: ")

                # Nieuwe highscore toevoegen aan database
                highscore_gegevens = """
                    INSERT INTO highscore (player_id, game_id, pogingen, high_score, highscore_datum)
                    VALUES (%s, %s, %s, %s, %s)
                """
                val_highscore = (
                    result["player_id"],
                    game_id_highscore,
                    pogingen,
                    high_score,
                    highscore_datum,
                )
                mycursor.execute(highscore_gegevens, val_highscore)
                db.commit()
                print("\nGelukt: alles is toegevoegd!")

                # Toon alle highscores van die speler
                mycursor.execute("SELECT * FROM highscore WHERE player_id = %s", (result["player_id"],))
                myresult = mycursor.fetchall()

                table = [
                    (
                        str(v["game_id"]),
                        str(v["player_id"]),
                        v["pogingen"],
                        v["high_score"],
                        v["highscore_datum"]
                    )
                    for v in myresult
                ]
                print(
                    tabulate(
                        table,
                        headers=["Game ID", "Player ID", "Pogingen", "Highscore", "Highscore Datum"],
                        tablefmt="grid",
                        stralign="left",
                    )
                )

            # -------------------- CASE 4 --------------------
            case "4":
                clear()
                # Alle games tonen
                select_all_games1 = "SELECT * FROM game"
                mycursor.execute(select_all_games1)
                myresult = mycursor.fetchall()

                table = [
                    (
                        str(z["game_id"]),
                        z["spelnaam"],
                        z["genre"],
                        f"€{float(z['prijs']):.2f}",
                    )
                    for z in myresult
                ]
                print(
                    tabulate(
                        table,
                        headers=["ID", "Spelnaam", "Genre", "Prijs"],
                        tablefmt="grid",
                        stralign="left",
                    )
                )

            # -------------------- CASE 5 --------------------
            case "5":
                clear()
                # Alle spelers tonen
                select_all_players = "SELECT * FROM player"
                mycursor.execute(select_all_players)
                myresult = mycursor.fetchall()

                table = [
                    (str(j["player_id"]), j["player_naam"], j["player_email"])
                    for j in myresult
                ]
                print(
                    tabulate(
                        table,
                        headers=["ID", "Naam", "Email"],
                        tablefmt="grid",
                        stralign="left",
                    )
                )

            # -------------------- CASE 6 --------------------
            case "6":
                clear()
                # Highscores per game bekijken
                game_highscore = """
                SELECT
                game.spelnaam,
                player.player_naam,
                highscore.high_score,
                highscore.highscore_datum
                FROM highscore
                JOIN game ON highscore.game_id = game.game_id
                JOIN player ON player.player_id = highscore.player_id;
                """

                mycursor.execute(game_highscore)
                myresult = mycursor.fetchall()

                table = [
                    (
                        str(b["spelnaam"]),
                        b["player_naam"],
                        b["high_score"],
                        b["highscore_datum"],
                    )
                    for b in myresult
                ]
                print(
                    tabulate(
                        table,
                        headers=[
                            "Game Naam",
                            "Player Naam",
                            "Highscore",
                            "Highscore Datum",
                        ],
                        tablefmt="grid",
                        stralign="left",
                    )
                )

            # -------------------- CASE 7 --------------------
            case "7":
                clear()
                # Ranglijst van spelers op highscore
                player_highscore = """
                SELECT
                player.player_naam,
                game.spelnaam,
                highscore.high_score
                FROM highscore
                JOIN game ON highscore.game_id = game.game_id
                JOIN player ON player.player_id = highscore.player_id
                ORDER BY high_score DESC;
                """

                mycursor.execute(player_highscore)
                myresult = mycursor.fetchall()

                table = [
                    (
                        c["player_naam"],
                        c["spelnaam"],
                        c["high_score"],
                    )
                    for c in myresult
                ]
                print(
                    tabulate(
                        table,
                        headers=["Player Naam", "Game Naam", "Highscore"],
                        tablefmt="grid",
                        stralign="left",
                    )
                )

            # -------------------- CASE 8 --------------------
            case "8":
                clear()
                # Winst per spel berekenen (pogingen * prijs)
                pogingen_highscore = """
                SELECT
                game.spelnaam,
                SUM(highscore.pogingen) AS pogingen,
                SUM(highscore.pogingen * game.prijs) AS winst
                FROM highscore
                JOIN game ON highscore.game_id = game.game_id
                GROUP BY game.spelnaam
                ORDER BY winst DESC;
                """

                mycursor.execute(pogingen_highscore)
                myresult = mycursor.fetchall()

                table = [(d["spelnaam"], d["pogingen"], d["winst"]) for d in myresult]
                print(
                    tabulate(
                        table,
                        headers=["Spelnaam", "Pogingen", "Winst"],
                        tablefmt="grid",
                        stralign="left",
                    )
                )

# Dit wordt uitgevoerd zodra je het programma afsluit
finally:
    mycursor.close()
    db.close()
    print("\nDatabaseverbinding gesloten. Programma gestopt.")