import os
import sqlite3
import pandas as pd
from etl import run_etl

def test_run_etl_creates_rows(tmp_path):
    csv = tmp_path / "input.csv"
    csv.write_text("product_id,product_name,price,quantity\n1,A,1.0,10\n2,B,2.0,20\n")
    db_file = tmp_path / "test.db"
    n = run_etl(csv_path=str(csv), db_path=str(db_file))
    assert n == 2
    conn = sqlite3.connect(str(db_file))
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM products")
    assert cur.fetchone()[0] == 2
    conn.close()

