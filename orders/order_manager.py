from . import MenuItem
from . import Order
import json


class OrderManager:
    def __init__(self):
        self.orders = []
        self.last_num = 0

    def create_order(self, table_num):
        self.last_num += 1
        order = Order(table_num)
        order.order_id = self.last_num
        self.orders.append(order)

    @staticmethod
    def get_menu():
        with open('orders/menu.json', 'r', encoding='utf-8') as menu_json:
            menu = json.load(menu_json)
            menu_list = []
            for item in menu:
                menu_list.append(MenuItem(**item))
        return menu_list

    @staticmethod
    def get_str_menu():
        drink = []
        snack = []
        hot = []
        dessert = []
        menu = OrderManager.get_menu()
        for item in menu:
            if item.category == 'Напиток':
                if not drink:
                    n = 1
                else:
                    n = len(drink)+1
                drink.append(f'{n}. {str(item)}')
            elif item.category == 'Закуска':
                if not snack:
                    n = 1
                else:
                    n = len(snack)+1
                snack.append(f'{n}. {str(item)}')
            elif item.category == 'Горячее блюдо':
                if not hot:
                    n = 1
                else:
                    n = len(hot)+1
                hot.append(f'{n}. {str(item)}')
            elif item.category == 'Десерт':
                if not dessert:
                    n = 1
                else:
                    n = len(dessert)+1
                dessert.append(f'{n}. {str(item)}')
        return drink, snack, hot, dessert