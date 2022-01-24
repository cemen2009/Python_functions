def show_magicians(magicians_list):
    """Write separately name of each magician from list"""
    for magician in magicians_list:
        print(f'{magician.title()}')


def make_great(magicians_list):
    """Add Great before name of each magician"""
    for i in range(0, len(magicians_list)):
        magicians_list[i] = "Great " + magicians_list[i]


magicians = ['sanya', 'tkach', 'mykola', 'cucumber']
show_magicians(magicians)
make_great(magicians)
show_magicians(magicians)
