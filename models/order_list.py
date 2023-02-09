from models.order import Order
import datetime as dt

order_list = [
    Order(dt.datetime(2020, 5, 17), "James Hetfield", "Microphone", 1, "sm58.jpeg"),
    Order(dt.datetime(2020, 5, 19), "Kirk Hammett", "Guitar", 5, "kirkguitar.jpeg"),
    Order(
        dt.datetime(2020, 5, 17),
        "Robert Trujillo",
        "Bass Guitar",
        1,
        "trujillobass.jpeg",
    ),
    Order(dt.datetime(2020, 5, 17), "Lars Ulrich", "Drum Kit", 3, "ulrichkit.jpeg"),
    Order(dt.datetime(2012, 7, 16), "Dimebag Darrell", "Razorback", 7),
]
