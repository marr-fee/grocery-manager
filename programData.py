import os
import json


def load_data():
    if os.path.exists('data/foodData.json'):
        try:
            with open('data/foodData.json', 'r') as file:
                FOOD_DATA = json.load(file)         
        except (json.JSONDecodeError, FileNotFoundError):
            print("Error Loading File")
    else:
        print("Loading Error")

    if os.path.exists('data/recipeData.json'):
        try:
            with open('data/recipeData.json', 'r') as file:
                RECIPES = json.load(file)
        except (json.JSONDecodeError, FileNotFoundError):
            print("Error Loading File")
    else:
        print("Loading Error")
    return FOOD_DATA, RECIPES



def dump_data():
    try:
        with open('data/foodData.json', 'w') as file:
            json.dump(FOOD_DATA, file, indent=4)
    except:
        print("Error Dumping File.")

    try:
        with open('data/recipeData.json', 'w') as file:
            json.dump(RECIPES, file, indent=4)
    except:
        print("Error Dumping File.")

FOOD_DATA, RECIPES = load_data()