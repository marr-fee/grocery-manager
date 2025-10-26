import recipes as recp
import inventory as inv
menu_options = {
  'title': 'Main Menu',
  'options': {
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

            '7' : {
                'title': 'Get Recipes',
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