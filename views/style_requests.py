import sqlite3
import json
from models import Style

STYLES = [
    {
        "id": 1,
        "style": "Classic",
        "price": 500
    },
    {
        "id": 2,
        "style": "Modern",
        "price": 710
    },
    {
        "id": 3,
        "style": "Vintage",
        "price": 965
    }
]

def get_all_styles():
    """returns all styles """
    # Open a connection to the database
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            s.id,
            s.style,
            s.price
        FROM styles s
        """)

    #initialize an empty list to hold all metal representations
    styles = []

    # Convert rows of data into a Python list
    dataset = db_cursor.fetchall()

    # Iterate list of data returned from database
    for row in dataset:
        style = Style(row['id'], row['style'], row['price'])

        styles.append(style.__dict__)
    
    return styles

# Function with a single parameter
def get_single_style(id):
    """returns a single requested style"""
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            s.id,
            s.style,
            s.price
        FROM style s
        WHERE s.id = ?
        """, ( id, ))

    # Load the single result into memory
    data = db_cursor.fetchone()

    style = Style(data['id'], data['style'], data['price'])

    return style.__dict__
    