import itemData as itmD
import userData as usrD


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

                border_len = 50

                if not header_printed:
                  print(f"{'— ' * border_len}")
                  print(f"|{'sn':^5}|{'Items'.upper():^30}|{'Qty':^8}|{'Size':^11}|{'Exp Date':^14}|{'Expires in':^14}|")
                  print(f"{'— ' * border_len}")
                  header_printed = True

                print(f"|{(i + 1):^5}|{name:^30}|{qty:^8}|{size+unit:^11}|{exp:^14}|{'Expires in':^14}|")
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

    print("Storage Options")
    print(f"1) Fridge\n2) Freezer")
    storage_location = input(f"Where Would You Like It Stored (Recommended: {best_storage}): ")
    return storage_location


def add_item():
    item = input("Enter The Item Name: ").strip().lower()

    item_data = itmD.get_item_details(item)
    storage = itmD.unpack_shelflife_data(item_data)
    unit = item_data.get("unit", None)
    item_size = get_item_size(unit)
    item_quantity = float(input("Enter The Quantity(e.g., 1 or 0.5 for half): "))
    expiry_date = input("Enter Expiry Date (YYYY-MM-DD): ").strip()
    item_storage = get_storage_location(item)






