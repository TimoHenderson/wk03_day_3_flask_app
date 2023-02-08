from models.order import Order
import datetime as dt

order_list = [
    Order(dt.datetime(2020, 5, 17), "James Hetfield", "Microphone", 1),
    Order(dt.datetime(2020, 5, 19), "Kirk Hammett", "Guitar", 5),
    Order(dt.datetime(2020, 5, 17), "Robert Trujillo", "Bass Guitar", 1),
    Order(dt.datetime(2020, 5, 17), "Lars Ulrich", "Drum Kit", 3),
]
