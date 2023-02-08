import datetime as dt


class Order:
    def __init__(self, order_date, customer_name, item_purchased, quantity):
        self.order_date = order_date
        self.customer_name = customer_name
        self.item_purchased = item_purchased
        self.quantity = quantity

    def date_as_string(self):
        return self.order_date.strftime("%a-%d-%b-%Y")

    def formatted_string(self):
        return f"{self.date_as_string()}, {self.customer_name}, {self.item_purchased}, {self.quantity}"
