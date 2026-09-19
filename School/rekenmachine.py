import School.berekeningen as berekeningen

def is_getal(waarde):
    try:
        float(waarde)
        return True
    except ValueError:
        return False

while True:
   keuze = input("Welke bewerking wil je invoeren? (+, -, *, /):")
   
   if keuze not in ["+", "-", "*", "/"]:
    print("Ongeldige keuze! Probeer het opnieuw.")
    continue
   
   a = input("Voer het eerste getal in: ")
   b = input("Voer het tweede getl in: ")
   
   if not (is_getal(a) and is_getal(b)):
    print("Fout: je moet een geldig getal invoeren!")
    continue
   
   a = float(a)
   b = float(b)

   if keuze == "+": 
      resultaat = berekeningen.optellen(a,b)
   elif keuze == "-":
      resultaat = berekeningen.aftrekken(a,b)
   elif keuze == "*":
      resultaat = berekeningen.vermenigvuldigen(a,b)
   else:
      resultaat = berekeningen.delen(a,b)
      
   print("Resultaat:", resultaat)
      
   doorgaan = input("Wil je doorgaan? (ja/nee?):")
   if doorgaan != "ja":
      print("Programma stopt. Tot ziens")
      break