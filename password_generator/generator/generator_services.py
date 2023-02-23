import random
from django.shortcuts import render


def generate_password(request, template, render_data):
    if request.method == 'GET':
        return render(request=request, template_name=template, context=render_data)
    else:
        try:
            return _create_password(request=request, render_data=render_data, template=template)
        except ValueError as e:
            render_data.update({'error': f'Bad date: {e}'})
            return render(request=request, template_name=template, context=render_data)


def _create_password(request, render_data, template):
    """ Create password. """
    password = _random_generator(request_data=request.POST)
    render_data.update({'password': password})
    return render(request, template, render_data)


def _random_generator(request_data: dict) -> str:
    """ Generate random password. """
    data = request_data
    length = int(data.get('length'))
    characters = _get_characters(data=data)
    password = ''

    for _ in range(length):
        password += random.choice(characters)

    return password


def _get_characters(data: dict) -> list:
    """ Create characters list. """

    base_characters = list('abcdefghijklmnopqrstuvwxyz')

    if data.get('uppercase'):
        base_characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if data.get('numbers'):
        base_characters.extend(list('1234567890'))
    if data.get('special'):
        base_characters.extend(list('!@#$%^&*()-_=+'))

    return base_characters
