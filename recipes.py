import programData as data


def generate_recipe(inventory):
    """ 
    Generates recipe suggestions based on user input and available ingredients.
    Filters recipes by category, time, servings, and allergies.
    Can use user inventory or random selection.
    """
    food_allergies = []
    food_categories = {
        '1': 'Breakfast',
        '2': 'Lunch',
        '3': 'Dinner',        
        '4': 'Dessert',        
        '5': 'Drinks',        
        '6': 'Cuisine'        
    }

    cook_times = {
        '1': 15,
        '2': 30,
        '3': 60
    }

    servings_type = {
        '1': '1-2',
        '2': 'Family',
        '3': 'Party-size'
    }

    print("Select a Category")
    print(f"1) Breakfast\n2) Lunch\n3) Dinner\n4) Dessert\n5) Drinks\n6) Cuisine")
    food_category = input("Select A Category: ").strip()
    food_category = food_categories.get(food_category)

    print("Do You Have Any Allergies?")
    print(f"1) Yes\n2) No")
    allergies = input("Select An Option: ")
    if allergies == '1':
        print("Please Let Us Know The Foods You Are Allergic To")
        print(f"\n1) Add Food Allergy\n2) Done")
        option = input("Enter An Option: ").strip()
        if option == '1':
            item = input("Enter Food Name: ").strip().capitalize()
            food_allergies.append(item)
        elif option == '2':
            print("Exiting")

    print("How Many Servings Do You Plan To Make?")
    print(f"1) 1-2\n2) Family\n3) Party-size\n")
    servings = input("Select An Option: ").strip()
    servings = servings_type.get(servings)

    print("Select A Cook Time Range")
    print(f"1) Under 15 min\n2) 30 min\n3) 1 hour+\n")
    cook_time = input("Select A Time Range: ").strip()
    cook_time = cook_times.get(cook_time)

    if inventory == 'own':
        print("Searching Your Inventory...")
        found = []
        for recipe in data.RECIPES: 
            if (recipe.get('category') == food_category 
            and recipe.get('time') == cook_time 
            and recipe.get('servings') == servings 
            and all(allrg not in [ingr['name'] for ingr in recipe['ingredients']] for allrg in food_allergies)):
                required = [ingr['name'] for ingr in recipe['ingredients']]
                missing = [ing for ing in required if ing not in data.INVENTORY]
        
            if not missing:
                found.append(recipe)
            else:
                print(f"\n🔸 You Could Make {recipe['name']} But The Following Ingredients Are Missing: {', '.join(missing)}")
                shopping_list_permission = input("Would You Like Me To Add This To Your Shopping List? (Yes / No): ").strip().lower()
                if shopping_list_permission == 'yes':
                    filename = input("Enter Filename: ")
                    generate_shopping_list(filename, missing)
                    print("✅ Items Saved To Shopping List.")
                    return
                elif shopping_list_permission == 'no':
                    return
            
        if not found:
            print("\nNo Recipes Found")
            return
        else:
            display_recipe(found)

    elif inventory == 'random':
        print("Generating Random Recipe...")
        found = [recipe for recipe in data.RECIPES 
                 if recipe.get('category') == food_category 
                 and recipe.get('time') == cook_time 
                 and recipe.get('servings') == servings 
                 and all(allrg not in [ingr['name'] for ingr in recipe['ingredients']] for allrg in food_allergies)]
        if not found:
            print("\nNo Recipes Found")
            return
        else:
            display_recipe(found)


def display_recipe(recipes_list):
    """ 
    Displays selected recipes with ingredients and steps.
    """
    recipe_text = ''
    
    for recipe in recipes_list:
        recipe_text += f"\n{recipe['image']} {recipe['name']} ({recipe['category']})"
        recipe_text += f"\nTime: {recipe['time']} min\nIngredients:"
        for ingredient in recipe['ingredients']:
            recipe_text += f"\n  - {ingredient['qty']} {ingredient['name']}"
        recipe_text += "\n\nSteps:"
        for i, step in enumerate(recipe['steps']):
            recipe_text += f"\n  {i+1}. {step}"
            recipe_text += "\n"
        
    print(recipe_text)


def generate_shopping_list(filename, items):
    """ 
    Saves missing ingredients to a shopping list text file.
    """
    with open(filename, 'w') as file:
        for itm in items:
            file.write(itm + '\n')
