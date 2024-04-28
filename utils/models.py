class OrderMapper:
    def __init__(self, order):
        self.order = order
        try:
            self.orderproduct = order.orderproduct_set.all()
        except:
            self.orderproduct = []
