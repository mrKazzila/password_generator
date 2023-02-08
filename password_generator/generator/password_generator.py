import random


def random_generator(request_data: dict):
    data = request_data
    base_characters = list('abcdefghijklmnopqrstuvwxyz')

    length = int(data.get('length'))
    if data.get('uppercase'):
        base_characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if data.get('numbers'):
        base_characters.extend(list('1234567890'))
    if data.get('special'):
        base_characters.extend(list('!@#$%^&*()-_=+'))

    password = ''
    for _ in range(length):
        password += random.choice(base_characters)

    return password
