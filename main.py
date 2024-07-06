from db import Database
import os
db = Database('data.db')


def tomenu():
    print('\nВернуться в гланое меню?')
    user_input = input("\nДа / Нет: ")
    if user_input.lower() == 'да':
        os.system('cls')
        menu()
    else:
        os.system('cls')
        print('Выход в меню не совершен')
        tomenu()

def get_all_rooms():
    os.system('cls')
    print('Все номера: ')
    print(db.get_all_rooms())
    tomenu()

def get_all_clients():
    if db.get_all_clients() == []:
        os.system('cls')
        print('Клиентов нету')
    else:
        os.system('cls')
        print('Все клиенты: ')
        print(db.get_all_clients())
    tomenu()

def make_order():
    if db.get_free_rooms() == []:
        os.system('cls')
        print('Свободных номеров нет. Оформление невозможно.')
    else:
        print('Начало оформление номера...')
        surname = input("\nВведите фамилию клиента: ")
        name = input("\nВведите имя клиента: ")
        lastname = input("\nВведите отчество клиента: ")
        phone = input("\nВведите телефон клиента: ")
        print('Свободные номера: ')
        print(db.get_free_rooms())
        room = input("\nВведите свободную компнату для клиента, из доступных выше: ")
        db.add_cliet(surname, name, lastname, phone, room)
        print('Регистрация окончена')
    tomenu()

def close_order():
    os.system('cls')
    print('Начало оформления выселения...')
    room = input("\nВведите номер комнаты: ")
    if db.get_room(room) == None:
        os.system('cls')
        print('Ошибка выселения! Комната свободна!')
    else:
        os.system('cls')
        print('\nВ комнате ' + room + ' сейчас проживает:')
        print(db.get_room(room))
        accept = input("\nВы действительно хотите произвести выселение комнаты " +room+"? (Да / Нет): ")
        if accept.lower() == 'да':
            os.system('cls')
            db.del_cliet(room)
            print('\nВыселение произведено успешно. Теперь комната '+room+ ' свободна.')
        else:
            menu()
    tomenu()

def busy_rooms():
    if db.get_busy_rooms() == []:
        os.system('cls')
        print('Занятых номеров нет')
    else:
        os.system('cls')
        print('Занятые номера: ')
        print(db.get_busy_rooms())
    tomenu()

def free_rooms():
    if db.get_free_rooms() == []:
        os.system('cls')
        print('Свободных номеров нет')
    else:
        os.system('cls')
        print('Свободные номера: ')
        print(db.get_free_rooms())
    tomenu()

def menu():
    os.system('cls')
    print('Панель управления OpenHotel.'
          '\nДля навигации введи цифру пункта меню')
    print('\n\n1.Все номера\n'
      '2.Свободные номера\n'
      '3.Занятые номера\n'
      '--------------------------\n'
      '4.Произвести бронирование\n'
      '5.Произвести выселение\n'
      '--------------------------\n'
      '6.Все клиенты')
    user_input = input('\nОжидание ввода:')
    if user_input == '1':
        get_all_rooms()
    if user_input == '2':
        free_rooms()
    if user_input == '3':
        busy_rooms()
    if user_input == '4':
        make_order()
    if user_input == '5':
        close_order()
    if user_input == '6':
        get_all_clients()
    else:1
        os.system('cls')
        menu()

if __name__ == '__main__':
    menu()