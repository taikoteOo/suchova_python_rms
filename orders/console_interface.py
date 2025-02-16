import sys
from . import Order
from . import OrderManager


class ConsoleInterface:
    def __init__(self, source):
        self.source = source

    def start(self):
        print('Выберете действие')
        print('1. Показать все заказы')
        print('2. Создать новый заказ')
        print('0. Выйти из системы')
        self.system_actions()

    def system_actions(self):
        action = input('>>> ')
        if action == '1':
            pass
        elif action == '2':
            self.new_order()
        elif action == '0':
            sys.exit()

    def new_order(self):
        print('Укажите номер стола')
        number = input('>>> ')
        self.source.create_order(number)
        print('Заказ успешно создан')
        self.order_menu()

    def show_order(self):
        pass

    def order_menu(self):
        print('Что делаем дальше?')
        print('1. Показать заказ')
        print('2. Добавить блюдо')
        print('3. Вернуться на главный экран')
        print('0. Выйти из системы')
        self.order_actions()

    def order_actions(self):
        action = input('>>> ')
        if action == '1':
            self.show_order()
        elif action == '2':
            self.menu_category()
        elif action == '3':
            self.start()
        elif action == '0':
            sys.exit()

    def show_menu(self):
        drink, snack, hot, dessert = OrderManager.get_str_menu()
        action = input('>>> ')
        if action == '1':
            print('\n'.join(drink))
        elif action == '2':
            print('\n'.join(snack))
        elif action == '3':
            print('\n'.join(hot))
        elif action == '4':
            print('\n'.join(dessert))
        elif action == '5':
            self.start()
        elif action == '0':
            sys.exit()

    def menu_category(self):
        print('Выберете категорию:')
        print('1. Напитки')
        print('2. Закуски')
        print('3. Горячие блюда')
        print('4. Дессерты')
        print('5. Вернуться на главный экран')
        print('0. Выйти из системы')
        self.show_menu()