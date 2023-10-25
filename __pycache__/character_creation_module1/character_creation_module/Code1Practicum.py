from random import randint

INTRO = '''РАССЧИТАЙ И ПОБЕДИ!
Загрузка...

Твоя цель — за 5 ходов набрать такое количество очков урона противнику,
которое попадет в диапазон +– 10 от значения здоровья противника.

Значение здоровья противника генерируется случайным образом
в диапазоне от 80 до 120 очков.

В твоём распоряжении три вида атак:
lite — урон от 2 до 5 очков;
mid — урон от 15 до 25 очков;
hard — урон от 30 до 40 очков.
ВПЕРЁД К ПОБЕДЕ!!!
'''

def set_enemy_health():
    return randint(80, 120)

def get_lite_attack():
    return randint(2, 5)

def get_mid_attack():
    return randint(15, 25)

def get_hard_attack():
    return randint(30, 40)

def compare_values(enemy_health, user_total_attack):
    point_difference = abs(enemy_health - user_total_attack)
    return 0 <= point_difference <= 10

def get_user_attack():
    total = 0
    attacks_types = {
        'lite': get_lite_attack,
        'mid': get_mid_attack,
        'hard': get_hard_attack,
    }

    for i in range(5):
        while True:
            input_attack = input('Введи тип атаки: ').lower()
            if input_attack in attacks_types:
                break
            else:
                print('Неверный тип атаки. Попробуй ещё раз.')

        attack_value = attacks_types[input_attack]()
        print(f'Количество очков твоей атаки: {attack_value}.')
        total += attack_value
    return total

def run_game():
    yes_no = {
        'Y': True,
        'N': False,
        'y': True,
        'n': False,
    }

    while True:
        print(INTRO)
        user_total_attack = get_user_attack()
        enemy_health = set_enemy_health()
        print(f'Тобой нанесён урон противнику равный {user_total_attack}.')
        print(f'Очки здоровья противника до твоей атаки: {enemy_health}.')
        if compare_values(enemy_health, user_total_attack):
            print('Ура! Победа за тобой!')
        else:
            print('В этот раз не повезло :( Бой проигран.')
        
        replay = input('Чтобы сыграть ещё раз, введи "y"; если не хочешь продолжать игру, введи "n": ')
        if replay not in yes_no:
            raise ValueError('Такой команды в игре нет.')
        if not yes_no[replay]:
            break

if __name__ == '__main__':
    run_game()
