def make_shirt(text, size='L'):
    """Return message about size of shirt and print on it"""
    print(f'Your shirt order:\nsize: {size.upper()};\nprint: "{text}".')


make_shirt('Hello world', 'xxl')
print()
make_shirt(text='fix my ass pls ^_^', size='s')
print()
make_shirt(text='I love anal')
