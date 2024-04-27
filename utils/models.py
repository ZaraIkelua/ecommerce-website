class OrderMapper:
    def __init__(self, order):
        self.order = order
        self.orderproduct = order.orderproduct_set.all()
