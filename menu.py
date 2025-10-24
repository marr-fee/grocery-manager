import recipes as recp
menu_options = {
  'title': 'Main Menu',
  'options': {
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