def models_build(wait_list, done_list):
    """Return list with done models"""
    print('Now we make models...')
    while wait_list:
        done_list.append(wait_list.pop())
        print(f'+ {done_list[-1]}')
    return done_list


def returning_done(done_list):
    """Rerurn models from done list"""
    print('The next model(s) are done:')
    for model in done_list:
        print(f'- {model}')
