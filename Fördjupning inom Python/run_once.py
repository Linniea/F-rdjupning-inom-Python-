import os
from etl import run_etl

# Hitta alltid den absoluta sökvägen till detta skript
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

csv_path = os.path.join(BASE_DIR, "data", "input.csv")
db_path = os.path.join(BASE_DIR, "data", "etl_data.db")

if __name__ == "__main__":
    run_etl(csv_path=csv_path, db_path=db_path)



