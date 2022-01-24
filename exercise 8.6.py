def city_country(city, country):
    """Return formatted message about city and country"""
    if len(country) <= 3:
        message = city.title() + ', ' + country.upper()
    else:
        message = city.title() + ', ' + country.title()
    return message


print(city_country('new york city', 'usa'))
print(city_country('malyn', 'ukraine'))
