#Opdracht 2
kleur = input("Wat is je favoriete kleur? ")
print (f"Jouw favoriete kleur is {kleur}")

woonplaats = input("Wat is jouw woonplaats? ")
print(f"Je woont in {woonplaats} ")

voornaam = input("Wat is jouw voornaam? ")
achternaam = input("Wat is jouw achternaam? ")
print(f"Jouw naam is {voornaam} {achternaam} ")

getal = input("Kies een getal onder de 100 ")
print(f"Jouw getal is {getal}")

getal1 = input("Kies een getal onder de 10 ")
getal2 = input("Kies nog een getal onder de 10 ")
getal1 = int(getal1)
getal2 = int(getal2)
getal_som = (getal1 * getal2)
print(f"Jouw getallen maal elkaar is {getal_som} ")

woord = input("Kies een willekurig woord ")
woord += woord
print(f"{woord}")

leeftijd = input("Hoe oud ben je? ")
print(f"Je bent {leeftijd} jaar oud")

dag = input("Wat is de dag van vandaag? ")
print(f"Vandaag is het {dag}")

huisdier = input("Noem 1 van jouw huisdieren? ")
naam_huisdier = input("Wat is de naam van jouw huisdier? ")
print(f"Jouw {huisdier} heet {naam_huisdier} ")

zin = input("Typ een korte zin ")
upper = zin.upper()
print (f"{upper}")