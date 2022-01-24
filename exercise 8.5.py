def describe_city(city, country='Ukraine'):
    """Return simple message about city in some country"""
    if len(country) <= 3:
        print(f'{city.title()} is in {country.upper()}.')
    else:
        print(f'{city.title()} is in {country.title()}.')


describe_city(city='new york city', country='usa')
describe_city('kyiv')
