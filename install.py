import sqlite3
import uuid
import random
import string

# Đường dẫn tới file cơ sở dữ liệu
DB_FILE = 'pos.db'

# Cấu trúc bảng Item
ITEM_TABLE = '''
CREATE TABLE IF NOT EXISTS Item (
    uuid TEXT PRIMARY KEY,
    name TEXT,
    price REAL,
    image TEXT
)
'''

# Cấu trúc bảng Order
ORDER_TABLE = '''
CREATE TABLE IF NOT EXISTS Orders (
    order_uuid TEXT PRIMARY KEY,
    item_uuid TEXT,
    quantity INTEGER,
    price REAL
);
'''

# Cấu trúc bảng OrderDetail
ORDER_DETAIL_TABLE = '''
CREATE TABLE IF NOT EXISTS OrderDetail (
    order_uuid TEXT PRIMARY KEY,
    item_uuid TEXT,
    quantity INTEGER,
    price REAL
)
'''

# Liên kết với bảng Order bằng cột uuid
ORDER_UUID_IDX = '''
CREATE INDEX IF NOT EXISTS order_uuid_idx ON OrderDetail (order_uuid)
'''

# Liên kết với bảng Item bằng cột uuid
ITEM_UUID_IDX = '''
CREATE INDEX IF NOT EXISTS item_uuid_idx ON OrderDetail (item_uuid)
'''

def create_tables():
    """Tạo cấu trúc bảng trong cơ sở dữ liệu"""
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()

    c.execute(ITEM_TABLE)
    c.execute(ORDER_TABLE)
    c.execute(ORDER_DETAIL_TABLE)
    c.execute(ORDER_UUID_IDX)
    c.execute(ITEM_UUID_IDX)

    # Thêm dữ liệu vào bảng Item
    # for i in range(10000):
    #     c.execute("INSERT INTO Item (uuid, name, price) VALUES (?,?,?)", (str(uuid.uuid4()), ''.join(random.choice(string.ascii_uppercase) for _ in range(8)), random.randint(100, 99999)))

    conn.commit()
    conn.close()

if __name__ == '__main__':
    product_name = ''.join(random.choice(string.ascii_uppercase) for _ in range(8))
    print(product_name)
    create_tables()
    print('Tables created.')
