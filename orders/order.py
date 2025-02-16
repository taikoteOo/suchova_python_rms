from . import MenuItem
from . import OrderManager
import json
from datetime import datetime as dt


class Order:
    def __init__(self, table_num):
        self.table_num = table_num
        self.order_id = None
        self.items = []
        self.total_price = 0
        self.created_at = dt.today()

    def add_item(self):
        menu = OrderManager.get_menu()