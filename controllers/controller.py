from flask import render_template
from app import app
from models.order_list import order_list


@app.route("/orders")
def orders():
    return render_template("index.html", order_list=order_list)


@app.route("/orders/<number>")
def order(number):
    return render_template("order.html", order=order_list[int(number)])
