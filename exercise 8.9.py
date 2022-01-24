def show_magicians(magicians_list):
    """Write separately name of each magician from list"""
    for magician in magicians_list:
        print(f'{magician.title()}')


magicians = ['sanya', 'tkach', 'mykola', 'cumber']
show_magicians(magicians)
