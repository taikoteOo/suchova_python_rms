from . import MenuItem
from . import Order

class OrderManager:
    def __init__(self):
        self.orders = []
        self.last_num = 0

    def create_order(self, table_num):
        self.last_num += 1
        order = Order(table_num)
        order.order_id = self.last_num
        self.orders.append(order)