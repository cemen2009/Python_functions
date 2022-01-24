def build_peron(first, last, **user_info):
    """Return dictionary about user"""
    user_dict = {'name': first, 'last name': last,}
    for key, value in user_info.items():
        user_dict[key] = value
    return user_dict


information = build_peron('sanya', 'xuy sosi', country='china', age=0, log='19.01.2007; 17:59:13')
print(information)
