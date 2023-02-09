from flask import render_template
from app import app
from models.order_list import order_list


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/orders")
def orders():
    return render_template("orders.html", order_list=order_list)


@app.route("/orders/<index>")
def order(index):
    chosen_order = order_list[int(index)]
    return render_template("order.html", order=chosen_order)
