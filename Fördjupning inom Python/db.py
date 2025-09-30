import sqlite3
import os

def init_db(db_path="data/etl_data.db"):
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS products (
        product_id INTEGER PRIMARY KEY,
        product_name TEXT,
        price REAL,
        quantity INTEGER
    )
    """)
    conn.commit()
    conn.close()

def upsert_products(data, db_path="data/etl_data.db"):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.executemany("""
    INSERT INTO products(product_id, product_name, price, quantity)
    VALUES (?, ?, ?, ?)
    ON CONFLICT(product_id) DO UPDATE SET
        product_name=excluded.product_name,
        price=excluded.price,
        quantity=excluded.quantity
    """, data)
    conn.commit()
    conn.close()

