# match - case (3.10>)
print('Возможные ходы:\n\tL - влево\n\tR - вправо\n\tF - прямо\n\tQ -выход')

while True:
    ch = input('Ваш выбор: ')
    match ch:
        case 'L'|'l'|'д'|'Д':
            print('Свернули налево')
        case 'R'|'r'|'к'|'К':
            print('Свернули направо')
        case 'F'|'f'|'а'|'А':
            print('Пошли прямо')
        case 'Q' | 'q' | 'й' | 'Й':
            print('До свидания')
            break
        case _: #default
            print('Выбор не ясен')