import sqlite3
import json
from models import Order, Metal, Style, Size


ORDERS =[
    {
        "id": 1,
        "metalId": 3,
        "sizeId": 2,
        "styleId": 3,
        "timestamp": 1614659931693
        }
]

def get_all_orders():
    """returns all orders"""
    # Open a connection to the database
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            o.id,
            o.metal_id,
            m.metal,
            m.price metal_price,
            o.size_id,
            z.size,
            z.price size_price,
            o.style_id,
            s.style,
            s.price style_price
        FROM Orders o
        JOIN Metals m
            ON m.id = o.metal_id
        JOIN Styles s
            ON s.id = o.style_id
        JOIN Sizes z
            ON z.id = o.size_id
        """)

    #initialize an empty list to hold all metal representations
    orders = []

    # Convert rows of data into a Python list
    dataset = db_cursor.fetchall()

    # Iterate list of data returned from database
    for row in dataset:
        order = Order(row['id'], row['metal_id'], row['size_id'], row['style_id'])

        metal= Metal(row['id'], row['metal'], row['metal_price'])
        order.metal = metal.__dict__

        style= Style(row['id'], row['style'], row['style_price'])
        order.style = style.__dict__

        size= Size(row['id'], row['size'], row['size_price'])
        order.size = size.__dict__

        orders.append(order.__dict__)

    return orders

def get_single_order(id):
    """returns a single requested order"""
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            o.id,
            o.metal_id,
            o.size_id,
            o.style_id
        FROM orders o
        WHERE o.id = ?
        """, ( id, ))

    # Load the single result into memory
    data = db_cursor.fetchone()

    order = Order(data['id'], data['metal_id'], data['size_id'], data['style_id'])

    return order.__dict__

def create_order(order):
    """function to creat new order"""
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Orders
            ( metal_id, size_id, style_id )
        VALUES
            ( ?, ?, ? );
        """, (order['metal_id'], order['size_id'], order['style_id'], ))

        id = db_cursor.lastrowid

        order['id'] = id

    return order

def delete_order(id):
    """function for delete an order"""
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM orders
        WHERE id = ?
        """, (id, ))


def update_order(id, new_order):
    """function to make changes to order"""
    # Iterate the ORDERS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, order in enumerate(ORDERS):
        if order["id"] == id:
            # Found the animal. Update the value.
            ORDERS[index] = new_order
            break
