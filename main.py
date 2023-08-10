import random


def get_choose():
    choose = int(input('Введите номер пункта: '))
    if type(choose) == int:
        if 1 > choose > 2:
            print('Ошибка: некорректный ввод.')
            get_choose()
        else:
            return choose


def get_result(main_player_item, player_item):
    if main_player_item == player_item:
        return 'Ничья'
    elif main_player_item == 'Камень':
        if player_item == 'Ножницы':
            return 1
        else:
            return 2
    elif main_player_item == 'Ножницы':
        if player_item == 'Бумага':
            return 1
        else:
            return 2
    elif main_player_item == 'Бумага':
        if player_item == 'Камень':
            return 1
        else:
            return 2


def get_player_choose():
    choose = int(input('Введите номер: '))
    if type(choose) is int:
        if 1 > choose > 3:
            print('Ошибка: Некорректный ввод.')
        else:
            return choose


def get_player_item(main_items):
    random_index = random.randint(0, len(main_items) - 1)
    return main_items[random_index]


def print_main_items(items):
    for i in range(len(items)):
        print(str(i+1) + ')' + items[i])


def play():
    print('\n\n')
    players = ['Кот', 'Жмуля', 'Лавандос', 'Ток']
    main_items = ['Камень', 'Ножницы', 'Бумага']

    player_for_game_index = random.randint(0, len(players) - 1)
    player_in_game = players[player_for_game_index]
    print(f'С вами будет играть: {player_in_game}!')
    player_item = get_player_item(main_items)
    print(f'{player_in_game}, уже что-то выбрал!')

    print('Выберете игровой элемент:')
    print_main_items(main_items)
    choose = get_player_choose()
    main_player_item = main_items[choose - 1]

    result = get_result(main_player_item, player_item)

    if result == 'Ничья':
        print(f'В этом раунде: {result}. Начинаем следующий раунд:')
        play()
    elif result == 1:
        print(f'В этом раунде победил: {USER_NAME}! У его противника был: {player_item}. Он проходит дальше.')
        play()
    else:
        print(f'В этом раунде победу одержал: {player_in_game}! У него был: {player_item}. {USER_NAME} нас покидает!')
        main()


def game_rules():
    print('''
Бумага побеждает камень («бумага обёртывает камень»).
Камень побеждает ножницы ( "камень затупляет ножницы ")
Ножницы побеждают бумагу («ножницы разрезают бумагу»).
''')
    main()


def main():
    print('\n\n')
    print(f'Добро пожаловать в игру камень-ножницы-бумага, {USER_NAME}!')

    print('1. Играть')
    print('2. Правила игры')

    choose = get_choose()
    if choose == 1:
        play()
    else:
        game_rules()


USER_NAME = input('Введите свое имя: ')
main()