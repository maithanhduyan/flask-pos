import sqlite3

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def save(self):
        conn = sqlite3.connect('pos.db')
        c = conn.cursor()

        c.execute("INSERT INTO Item (name, price) VALUES (?, ?)", (self.name, self.price))

        conn.commit()
        conn.close()

    @staticmethod
    def get_all():
        conn = sqlite3.connect('pos.db')
        c = conn.cursor()

        c.execute("SELECT * FROM Item")
        items = c.fetchall()

        conn.close()

        return items
