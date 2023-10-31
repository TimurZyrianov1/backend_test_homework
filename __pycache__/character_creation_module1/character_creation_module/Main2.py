from random import randint


def attack(char_name: str, char_class: str) -> str:
    """
    Рассчитайте и верните урон, нанесенный атакой персонажа.

    Args:
        char_name (str): Имя персонажа.
        char_class (str): Класс персонажа (warrior, mage, or healer).

    Returns:
        str: Сообщение, указывающее на нанесенный ущерб.
    """
    if char_class == 'warrior':
        return (f'{char_name} нанёс противнику урон, '
                f'равный {5 + randint(3, 5)}')
    if char_class == 'mage':
        return (f'{char_name} нанёс противнику урон, '
                f'равный {5 + randint(5, 10)}')
    if char_class == 'healer':
        return (f'{char_name} нанёс противнику урон, '
                f'равный {5 + randint(-3, -1)}')


def defence(char_name: str, char_class: str) -> str:
    """
    Рассчитайте и верните урон, заблокированный защитой персонажа.

    Args:
        char_name (str): Имя персонажа.
        char_class (str): Класс персонажа (warrior, mage, or healer).

    Returns:
        str: Сообщение с указанием суммы заблокированного ущерба.
    """
    if char_class == 'warrior':
        return (f'{char_name} блокировал '
                f'{10 + randint(5, 10)} урона')
    if char_class == 'mage':
        return (f'{char_name} блокировал '
                f'{10 + randint(-2, 2)} урона')
    if char_class == 'healer':
        return (f'{char_name} блокировал '
                f' {10 + randint(2, 5)} урона')


def special(char_name: str, char_class: str) -> str:
    """
    Вычислите и верните результат использования особой способности персонажа.

    Args:
        char_name (str): Имя персонажа.
        char_class (str): Класс персонажа (warrior, mage, or healer).

    Returns:
    str: Сообщение, указывающее на результат
    применения специальной способности.
    """
    if char_class == 'warrior':
        return (f'{char_name} применил специальное умение «Выносливость '
                f'{80 + 25}»')
    if char_class == 'mage':
        return (f'{char_name} применил специальное умение «Атака '
                f'{5 + 40}»')
    if char_class == 'healer':
        return (f'{char_name} применил специальное умение «Защита '
                f'{10 + 30}»')


def start_training(char_name: str, char_class: str) -> str:
    """
    Начать тренировку персонажа.

    Args:
        char_name (str): Имя персонажа.
        char_class (str): Класс персонажа (warrior, mage, or healer).

    Returns:
        str: Сообщение о завершении тренировки.
    """
    if char_class == 'warrior':
        print(f'{char_name}, ты Воитель — отличный боец ближнего боя.')
    if char_class == 'mage':
        print(f'{char_name}, ты Маг — превосходный укротитель стихий.')
    if char_class == 'healer':
        print(f'{char_name}, ты Лекарь — чародей, способный исцелять раны.')
    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: '
          f'{attack}, — чтобы атаковать противника, '
          f'{defence}, — чтобы блокировать атаку противника или'
          f'{special}, — чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd = None
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        if cmd == 'defence':
            print(defence(char_name, char_class))
        if cmd == 'special':
            print(special(char_name, char_class))
    return 'Тренировка окончена.'


def choice_char_class() -> str:
    """
    Выбор класса персонажа.

    Returns:
        str: Выбранный класс персонажа (warrior, mage, или healer).
    """
    approve_choice = None
    char_class = None
    while approve_choice != 'y':
        char_class = input(
            'Введи название персонажа, '
            'за которого хочешь играть: '
            'Воитель — warrior, Маг — mage, Лекарь — healer ',

        )
        char_class = char_class.strip().lower()

        if char_class == 'warrior':
            print(
                'Воитель — дерзкий воин ближнего боя. '
                'Сильный, выносливый и отважный.',
            )
        elif char_class == 'mage':
            print(
                'Маг — находчивый воин дальнего боя. '
                'Обладает высоким интеллектом.',
            )
        elif char_class == 'healer':
            print(
                'Лекарь — могущественный заклинатель. '
                'Черпает силы из природы, веры и духов.',
            )
        else:
            print('Некорректный выбор. Пожалуйста, выберите из доступных')
            print('классов.')

    approve_choice = input(
        'Нажми (Y), чтобы подтвердить выбор, '
        'или любую другую кнопку, '
        'чтобы выбрать другого персонажа: ',
    ).strip().lower()

    return char_class


if __name__ == '__main__':
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name: str = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class: str = choice_char_class()
    print(start_training(char_name, char_class))
