import programData as dta

def abbiviate_unit(unit):
    if unit == "liters":
        return 'L'
    if unit == "milliliters":
        return 'ml'
    if unit == "kilograms":
        return 'kg'
    if unit == "grams":
        return 'g'
    if unit == "pieces":
        return 'pcs'
    if unit == "bunches":
        return 'bnch'


def get_item_details(item):
    """ 
    Retrieves all stored details about a specific food item.
    """
    classes = dta.FOOD_DATA["classes"]
    units = dta.FOOD_DATA["units"]
    storage = dta.FOOD_DATA["storage"]

    # Find class
    for key, values in classes.items():
        if item in values:
            item_class = key
            break

    # Find unit
    for key, values in units.items():
        if item in values:
            item_unit = key
            abbr_unit = abbiviate_unit(item_unit)
            break

    # Find storage info
    for key, data in storage.items():
        if item.lower() == key:
            item_category = data.get('category', 'unknown')
            is_perishable = data.get('perishable', 'unknown')
            has_open_state = data.get('hasOpenedState', 'unkown')
            best_storage = data.get('bestStoredIn', 'unknown')
            possible_storage_locations = data.get('canBeStoredIn', [])
            storage_options = data.get('storageOptions', {})
            break

    if not item_class or not item_unit or not item_category:
        print(f"⚠️ Warning: '{item}' not found in FOOD DATA.")
        return None

    return {
        "name": item,
        "class": item_class,
        "unit": item_unit,
        "abbr_unit": abbr_unit,
        "category": item_category,
        "perishable": is_perishable,
        "hasOpenedState": has_open_state,
        "bestStoredIn": best_storage,
        "canBeStoredIn": possible_storage_locations,
        "storageOptions": storage_options
    }


def unpack_shelflife_data(data):
    """ 
    Extracts and organizes the shelf life information for an item.
    """
    storage_info = {}
    storage_options = data.get('storageOptions', {})
    possible_locations = data.get('canBeStoredIn', [])
    has_opened_state = data.get('hasOpenedState', False)

    for loc in possible_locations:
        loc_data = storage_options.get(loc, {})
        if has_opened_state:
            storage_info[loc] = {
                "opened": loc_data.get("opened", 0),
                "unopened": loc_data.get("unopened", 0)
            }
        else:
            storage_info[loc] = {
                "default": loc_data.get("default", 0)
            }

    return storage_info


def print_item_info():
    """ 
    Prints a descriptive summary of a specific food item.  
    """
    item = input("Enter Item Name: ").strip().lower()
    data = get_item_details(item)
    shelflife = unpack_shelflife_data(data) 

    item_class = data.get('class', 'unknown')
    item_category = data.get("category", "unknown")
    item_measurement_unit = data.get("unit", "unit")
    best_storage = data.get("bestStoredIn", "fridge")
    has_opened_state = data.get("hasOpenedState", False)

    description_parts = []
    follow_up_description = []

    # Handle opened/unopened items
    if has_opened_state:
        for loc, values in shelflife.items():
            opened = values.get("opened", None)
            unopened = values.get("unopened", None)
            if opened is not None and unopened is not None:
                if best_storage == loc:
                    description_parts.append(
                        f"up to {unopened} days unopened and {opened} days if opened"
                    )
                else:
                    follow_up_description.append(
                        f"It can also be stored in the {loc}, where it typically lasts up to {unopened} days unopened and {opened} days if opened."
                    )
    else:
        # Handle default (non-opened) items
        for loc, values in shelflife.items():
            default = values.get("default", None)
            if default is not None:
                if best_storage == loc:
                    description_parts.append(
                        f"around {default} days in the {loc}"
                    )
                else:
                    follow_up_description.append(
                        f"It can also be stored in the {loc}, where it typically lasts up to {default} days if opened."
                    )

    # Combine the dynamic parts into a natural sentence
    storage_sentence = ", ".join(description_parts)
    follow_up_storage_sentence = ", ".join(follow_up_description)

    print(
        f"\n{item.capitalize()} is a {item_category} product of the {item_class} food class and is typically measured in {item_measurement_unit}. "
        f"It’s best stored in the {best_storage}, lasting {storage_sentence}. "
        f"{follow_up_storage_sentence}"
    )

def print_storage_tips(item):
    for key , value in dta.FOOD_DATA["storage"].items():
        if key == item:
            print(f"Storage Tip: {value["storageTip"]}")

