def sandwich_describe(*toppings_list):
    """Describe the sandwich"""
    print('Sandwich toppings:')
    for topping in toppings_list:
        print(f'- {topping}')


sandwich_describe('sous', 'kartoshka', 'pitsa')
sandwich_describe('rusnya')
sandwich_describe('xlib', 'kotleta', 'kapustka', 'grenochki')
