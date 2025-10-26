import programData as data

def update_all_inventory(inventory):
    all_items = [item for section in inventory if section['name'] != 'all' for item in section['items']]
    for section in inventory:
        if section['name'] == 'all':
            section['items'] = all_items
            break

def display_inventory(location):
    update_all_inventory(data.INVENTORY)

    print(f"{'=' * 15}")
    print(f"{location.capitalize().center(15)}")    
    print("===============")   
    for item in data.INVENTORY:
        if item['name'] == location:
            header_printed = False
            for i, itm in enumerate(item['items']):
                
                name = itm.get('name', 'unknown')
                exp = itm.get('expiry date', 'unknown')
                qty = itm.get('quantity', 0)
                size = str(itm.get('size', 0))
                unit = str(itm.get('unit', 'unknown'))

                #S = space
                nS = len(name)+4
                eS = len(exp)+4
                qS = len(str(qty))+4
                sS = (len(size)+ len(unit))+4
                n_s = len(str(i))+4

                full_len = (nS+eS+qS+sS+n_s)//2

                if not header_printed:
                  print(f"{'— ' * full_len}")
                  print(f"|{'sn':^{n_s}}|{'Item':^{nS}}|{'Qty':^{qS}}|{'Size':^{sS}}|{'Exp Date':^{eS}}|")
                  print(f"{'— ' * full_len}")
                  header_printed = True

                print(f"|{i:^{n_s}}|{name:^{nS}}|{qty:^{qS}}|{size+unit:^{sS}}|{'Exp Date':^{eS}}|")
                print(f"{'— ' * full_len}")




