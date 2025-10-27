import itemData as itmD
import userData as usrD
from datetime import datetime



def update_all_inventory(inventory):
    all_items = [item for section in inventory if section['name'] != 'all' for item in section['items']]
    for section in inventory:
        if section['name'] == 'all':
            section['items'] = all_items
            break

def display_inventory(location):
    update_all_inventory(usrD.USER_DATA["inventory"])

    for item in usrD.USER_DATA["inventory"]:
        if item['name'] == location:
            header_printed = False
            for i, itm in enumerate(item['items']):
                
                name = itm.get('name', 'unknown')
                exp = itm.get('expiry date', 'unknown')
                qty = itm.get('quantity', 0)
                size = str(itm.get('size', 0))
                unit = str(itm.get('abbr_unit', 'unknown'))
                days_till_exp = itm.get('days_till_exp', 'unknown')

                border_len = 50

                if not header_printed:
                  print(f"{'— ' * border_len}")
                  print(f"|{'sn':^5}|{'Items'.upper():^30}|{'Qty':^8}|{'Size':^11}|{'Exp Date':^14}|{'Expires in':^14}|")
                  print(f"{'— ' * border_len}")
                  header_printed = True

                print(
                        f"|{(i + 1):^5}"
                        f"|{name:^30}"
                        f"|{qty:^8}"
                        f"|{size + unit:^11}"
                        f"|{exp:^14}"
                        f"|{(str(days_till_exp) + ' day' + ('s' if int(days_till_exp) > 1 else '')):^14}|"
                    )

                print(f"{'— ' * border_len}")

def get_item_size(unit):
    """
    Returns a customized input prompt message depending on the unit of measure.
    """
    if unit == 'liters':
        prompt = "Enter the size in liters (e.g., 1 for 1L bottle, 0.5 for 500ml): "
    elif unit == 'milliliters':
        prompt = "Enter the size in milliliters (e.g., 250 for a small bottle, 1000 for 1L): "
    elif unit == 'kilograms':
        prompt = "Enter the size in kilograms (e.g., 1 for 1kg pack, 0.25 for 250g): "
    elif unit == 'grams':
        prompt = "Enter the size in grams (e.g., 500 for 500g pack): "
    elif unit == 'pieces':
        prompt = "Enter the size or count in pieces (e.g., 1 for one loaf, 2 for two bars): "
    elif unit == 'bunches':
        prompt = "Enter the size in bunches (e.g., 1 for one bunch, 0.5 for half a bunch): "
    else:
        prompt = f"Enter the size in {unit}: "

    size = input(prompt)
    return float(size)


def get_storage_location(item):
    item_data = itmD.get_item_details(item)
    best_storage = item_data.get("bestStoredIn", None)

    print("\nStorage Options")
    while True:
        print("1) Fridge\n2) Freezer\n3) Pantry")
        option = input(f"Where Would You Like It Stored? (Recommended: {best_storage}) ")

        if option == '1':
            return 'fridge'
        elif option == '2':
            return 'freezer'
        elif option == '3':
            return 'pantry'
        else:
            print(f"Invalid choice — recommended location: {best_storage}")
            


def get_time_till_expiry(year, month, day):
    today = datetime.now()
    formatted_date_today = today.strftime("%Y-%m-%d")
    target_date = datetime(int(year), int(month_map[month]), int(day), 23, 0, 0)
    difference = target_date - today
    days_till_exp = difference.days
    return formatted_date_today, days_till_exp

month_map = {
        "JAN": 1,
        "FEB": 2,
        "MAR": 3,
        "APR": 4,
        "MAY": 5,
        "JUN": 6,
        "JUL": 7,
        "AUG": 8,
        "SEP": 9,
        "OCT": 10,
        "NOV": 11,
        "DEC": 12
    }

def validate_date_input(date: str, is_perishable: bool):

    parts = date.split("-") if "-" in date else date.split(" ")
    
    if is_perishable:
        if len(parts) != 3 or len(parts[0]) != 4 or len(parts[1]) != 3 or len(parts[2]) != 2:
            return False, None
        elif parts[1].upper() not in month_map.keys():
            return False, None
        else:
            year, month, day = parts
            return True, (year, month.upper(), day)
    if not is_perishable:
        if len(parts) != 2 or len(parts[0]) != 3 or len(parts[1]) != 4:
            return False, None
        elif parts[0].upper() not in month_map.keys():
            return False, None
        else:
            month, year = parts
            day = '1'
            return True, (day, month.upper(), year) 

def add_item():
    
    item = input("Enter The Item Name: ").strip().lower()

    item_data = itmD.get_item_details(item)
    storage = itmD.unpack_shelflife_data(item_data)
    unit = item_data.get("unit", None)
    abbr_unit = item_data.get("abbr_unit", "unknown")
    item_size = get_item_size(unit)
    item_quantity = int(input("Enter The Quantity(e.g., 1 or 0.5 for half): "))

    is_perishable = item_data.get("perishable", None)
    if is_perishable:
        print("When Does This Item Expire? (e.g 2025-OCT-20 or 2025 OCT 20)")
        while True:
            expiry_date = input("Enter Expiry Date (YYYY-MMM-DD or YYYY MMM DD): ").strip().upper()
            is_valid_date_format, date_format = validate_date_input(expiry_date, True)
            if is_valid_date_format:
                year, month, day = date_format
                break
            else:
                print("Invalid Date Format") 

    elif not is_perishable:
        print("When Does This Item Expire? (e.g JAN-2029 or JAN 2029)")
        while True:
            expiry_date = input("Enter Expiry Date (MMM-YYYY or MMM YYYY): ").strip()
            is_valid_date_format, date_format = validate_date_input(expiry_date, False)
            if is_valid_date_format:
                day, month, year = date_format
                break
            else:
                print("Invalid Date Format")

    formatted_date_today, days_till_exp = get_time_till_expiry(year, month.upper(), day)

    item_storage = get_storage_location(item)
    
    new_item = {
        'name': item,
        'quantity': item_quantity,
        'size': item_size,
        'best_storage': item_storage,
        'expiry date': expiry_date,
        'date_added': formatted_date_today,
        'abbr_unit': abbr_unit,
        'days_till_exp':  days_till_exp
    }

    update_inventory(new_item)
    update_all_inventory(usrD.USER_DATA['inventory'])

def update_inventory(new_item):
    item_storage = new_item['best_storage']

    for location in usrD.USER_DATA['inventory']:
        if location['name'] == item_storage:
            location['items'].append(new_item)
            print(f"{new_item['name']} added to {item_storage}.")
            break

            






