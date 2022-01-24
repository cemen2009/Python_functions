def car_dictionary(manufacturer, model, **args):
    """Return dictionary about car"""
    dictionary = {'Manfacturer': manufacturer, 'Model': model,}
    for key, value in args.items():
        dictionary[key] = value
    return dictionary


mitsubishi = car_dictionary('mitsubishi', 'model xuy', color='yellow', equipment='full')
print(mitsubishi)
