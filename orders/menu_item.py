import json


class MenuItem:
    def __init__(self, name: str, price: float, weight: int, category: str):
        self.name = name
        self.price = price
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name} ({self.weight} г(мл)) - {self.price} у.е.'