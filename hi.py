import random
def fraz():
    phrases = [
        'Привет',
        'Добрый день',
        'Пока'
    ]
    show_index = random.randint(0, 2)
    return phrases[show_index] + '!'