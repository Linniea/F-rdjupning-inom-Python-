import sqlite3, os

db = os.path.join(os.getcwd(), "data", "etl_data.db")
conn = sqlite3.connect(db)
cur = conn.cursor()
cur.execute("SELECT * FROM products ORDER BY product_id")
rows = cur.fetchall()
for r in rows:
    print(r)
conn.close()

