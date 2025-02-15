import json


class MenuItem:
    def __init__(self, item_name: str):
        item = self.get_item(item_name)
        self.name = item['name']
        self.price = item['price']
        self.weight = item['weight']
        self.category = item['category']

    def __str__(self):
        return f'{self.name} ({self.weight} г(мл)) - {self.price} у.е.'

    def get_item(self, item_name: str):
        menu = self.get_menu()
        for item in menu:
            if item['name'].lower() == item_name.lower():
                return item

    @staticmethod
    def get_menu():
        with open('menu.json', 'r', encoding='utf-8') as menu_json:
            menu = json.load(menu_json)
        return menu

    def get_str_menu(self):
        str_menu = ''
        menu = self.get_menu()
        for item in menu:
            str_menu += self.__str__() + '\n'
        return str_menu

b = MenuItem('борщ')
print(b.get_str_menu())