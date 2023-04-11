import sqlite3
import uuid
import random
import string

# Đường dẫn tới file cơ sở dữ liệu
DB_FILE = 'pos.db'

def insert_demo_data():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()

    # Thêm dữ liệu vào bảng Item
    for i in range(100):
        uuid1 = str(uuid.uuid4())
        name = ''.join(random.choice(string.ascii_uppercase) for _ in range(8))
        price = random.randint(100, 99999)
        c.execute("INSERT INTO Item (uuid, name, price) VALUES (?,?,?)", (uuid1, name, price))

  
    conn.commit()
    conn.close()

def delete_all_items():
    """Xóa toàn bộ dữ liệu của bảng Item"""
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()

    c.execute("DELETE FROM Item")

    conn.commit()
    conn.close()

def main():
    delete_all_items()
    insert_demo_data()

if __name__ == '__main__':
    main()
    print('Data Demo created.')
