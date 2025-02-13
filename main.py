from orders import MenuItem, Order, OrderManager, ConsoleInterface

def main():
    order_man = OrderManager()
    console = ConsoleInterface(source = order_man)

    while True:
        console.start()


if __name__ == '__main__':
    main()