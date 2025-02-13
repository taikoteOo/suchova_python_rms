import json


class MenuItem:
    def __init__(self, item_name):
        item = self.get_item('menu.json', item_name=item_name)
        self.name = item['name']
        self.price = item['price']
        self.weight = item['weight']
        self.category = item['category']

    def __str__(self):
        return f'{self.name} ({self.weight} г(мл)) - {self.price} у.е.'

    @staticmethod
    def get_item(menu_json, item_name: str):
        with open(menu_json, 'r', encoding='utf-8') as menu_file:
            menu = json.load(menu_file)

        for item in menu:
            if item['name'].lower() == item_name.lower():
                return item