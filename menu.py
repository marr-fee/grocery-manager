import recipes as recp
import inventory as inv
import itemData as itmD
menu_options = {
  'title': 'Main Menu',
  'options': {
            '1' : {
                'title': 'Add Item',
                #'options': add_item
                    },
            '2' : {
                'title': 'Get Info On Item',
                'options': itmD.print_item_info
                    },
            '3' : {
                'title': 'View Inventory',
                'options': {
                        '1' : {
                        'title': 'Fridge',
                        'options': (inv.display_inventory, 'fridge')
                    },
                    '2' : {
                        'title': 'Freezer',
                        'options': (inv.display_inventory, 'freezer')
                    },
                    '3' : {
                        'title': 'Pantry',
                        'options': (inv.display_inventory, 'pantry')
                    },
                    '4' : {
                        'title': 'View All',
                        'options': (inv.display_inventory, 'all')
                    }
                }                    
                    },
            '6' : {
                'title': 'Remove Item',
                #'options': check_item_expiry                  
                    },
            '7' : {
                'title': 'Recipe Suggestions',
                'options': {
                    '1': {
                        'title': 'Generate From Ingredients You Have',
                        'options': (recp.generate_recipe, 'own')
                    },
                    '2': {
                        'title': 'Generate Random Recipe',
                        'options': (recp.generate_recipe, 'random')
                    }
                }
            }
  }
}