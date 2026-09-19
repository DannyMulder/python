from flask import Flask, render_template, request
import requests
import json, os
from concurrent.futures import ThreadPoolExecutor

BASE_DIR = os.path.dirname(os.path.abspath(__file__)) 
json_path = os.path.join(BASE_DIR, "ingredients.json")

"""Open json ingredients""" 
with open(json_path, "r", encoding="utf-8") as f:
    ingredients_json = json.load(f)["ingredients"]

"""Get all drinks"""
def Fecth_Letter(letter):
    url = f"https://www.thecocktaildb.com/api/json/v1/1/search.php?f={letter}"
    responce = requests.get(url, timeout=5).json()
    return responce.get("drinks", [])

def GetAllDrinks():
    drinks = []
    
    letters = "abcdefghijklmnopqrstuvwxyz"
    
    with ThreadPoolExecutor(max_workers=26) as executer:
        results = executer.map(Fecth_Letter, letters)
        
        for drink in results:
            if drink:
                drinks.extend(drink)
    
    return drinks

"""Store drinks"""
RESULTS_DRINKS = []

"""Debug all drinks"""
try: 
    ALL_DRINKS = GetAllDrinks() 
    print(f"Loaded {len(ALL_DRINKS)} drinks.") 
except Exception as e: 
    print("Error loading drinks:", e)

"""Sort all drinks"""
def GetAndSort(alcoholic_only, category, sort):
    global ALL_DRINKS
    drinks = ALL_DRINKS
    
    if (alcoholic_only):
        drinks = [d for d in drinks if d["strAlcoholic"] == "Alcoholic"]
    if (category):
        drinks = [d for d in drinks if d["strCategory"] == category]
    if (sort):
        if sort == "A-Z":
            drinks.sort(key=lambda d: d["strDrink"])
        elif sort == "Z-A":
            drinks.sort(key=lambda d: d["strDrink"], reverse=True)
        else:
            drinks = [d for d in drinks if d["strDrink"].startswith(sort)]
    return drinks

def IngredientsSort(drinks, ingredient):
    SortedDrinks = []
    for drink in drinks:
        for i in range(1, 16):
            currentDrink = drink[f"strIngredient{i}"]
            if currentDrink != None and currentDrink.strip().lower() == ingredient.strip().lower():
                SortedDrinks.append(drink)
    
    return SortedDrinks        

"""Main app"""
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def Index():
    global RESULTS_DRINKS, ALL_DRINKS
    if request.method == "POST":
        cocktail = request.form.get("cocktail")
        alcoholic_only = request.form.get("alcoholic")
        category = request.form.get("category")
        sort = request.form.get("sort")
        ingredient = request.form.get("ingredient")
        selectAll = request.form.get("selectAll")
        
        if selectAll:
            showAll = bool(sort or category or alcoholic_only or selectAll)
        else: showAll = False

        if showAll:
            drinks = GetAndSort(alcoholic_only, category, sort)

            if ingredient:
                drinks = IngredientsSort(drinks, ingredient)
            
            RESULTS_DRINKS = drinks        
            return AllDrinks(RESULTS_DRINKS, cocktail, False)
        else:
            if cocktail == None or cocktail == "":
                return render_template("index.html", ingredients=ingredients_json, drinks=ALL_DRINKS)
            
            drink = [d for d in ALL_DRINKS if d["strDrink"] == cocktail]
            
            return AllDrinks(drink, cocktail, True)
    return render_template("index.html", ingredients=ingredients_json, drinks = ALL_DRINKS)

"""Return the results"""
def AllDrinks(drinks, cocktail, specific):
    global ALL_DRINKS
    if len(ALL_DRINKS) == 0:
        ALL_DRINKS = GetAllDrinks() 

    if len(RESULTS_DRINKS) == 1 and not specific:
        selected = RESULTS_DRINKS[0]
    elif specific: selected = next((d for d in drinks if d["strDrink"] == cocktail), "")
    else: selected = ""

    return render_template("results.html", 
            drinks=drinks, 
            selected=selected,
            index=0
            )

"""Return the clicked drink"""
@app.route("/showSelected", methods=["GET"])
def ShowSelected():
    cocktail = request.args.get("cocktail")

    selected = next(
        (d for d in RESULTS_DRINKS if d["strDrink"].strip().lower() == cocktail.strip().lower()),
        RESULTS_DRINKS[0]
    )

    return render_template("results.html", 
            drinks=[RESULTS_DRINKS[0]], 
            selected=selected
            )

"""Return to index.html"""
@app.route("/Return", methods=["GET"])
def PopUp():
    return render_template("index.html", ingredients=ingredients_json, drinks = ALL_DRINKS)

"""Return new page index"""
@app.route("/NewIndex", methods=["GET"])
def NewIndex():
    index = int(request.args.get("index"))
    
    return render_template("results.html", 
        drinks=RESULTS_DRINKS, 
        selected="",
        index=index
        )

"""Runs main app"""
if __name__ == "__main__":
    app.run(debug=True)