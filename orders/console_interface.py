import sys
from . import Order


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
            pass
        elif action == '3':
            self.start()
        elif action == '0':
            sys.exit()