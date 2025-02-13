from . import MenuItem


class Order:
    def __init__(self, table_num):
        self.table_num = table_num
        self.order_id = None
        self.items = []
        self.total_price = 0
        self.created_at = None

    def search_item(self, item: str):
        pass
