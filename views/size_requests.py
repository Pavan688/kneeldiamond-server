import sqlite3
import json
from models import Size

SIZES = [
    {
        "id": 1,
        "carets": 0.5,
        "price": 405
    },
    {
        "id": 2,
        "carets": 0.75,
        "price": 782
    },
    {
        "id": 3,
        "carets": 1,
        "price": 1470
    },
    {
        "id": 4,
        "carets": 1.5,
        "price": 1997
    },
    {
        "id": 5,
        "carets": 2,
        "price": 3638
    }
]

def get_all_sizes():
    """returns all sizes"""
    # Open a connection to the database
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            z.id,
            z.size,
            z.price
        FROM sizes z
        """)

    #initialize an empty list to hold all metal representations
    sizes = []

    # Convert rows of data into a Python list
    dataset = db_cursor.fetchall()

    # Iterate list of data returned from database
    for row in dataset:
        size = Size(row['id'], row['size'], row['price'])

        sizes.append(size.__dict__)
    
    return sizes

# Function with a single parameter
def get_single_size(id):
    """returns a single requested size"""
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            z.id,
            z.size,
            z.price
        FROM sizes z
        WHERE z.id = ?
        """, ( id, ))

    # Load the single result into memory
    data = db_cursor.fetchone()

    size = Size(data['id'], data['size'], data['price'])

    return size.__dict__
    