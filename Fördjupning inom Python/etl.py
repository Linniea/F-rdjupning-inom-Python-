import pandas as pd
from db import init_db, upsert_products
from logger_conf import get_logger

logger = get_logger(__name__)

def run_etl(csv_path="data/input.csv", db_path="data/etl_data.db"):
    try:
        df = pd.read_csv(csv_path)
        logger.info(f"Läste {len(df)} rader från {csv_path}")
        data = df.to_records(index=False).tolist()
        init_db(db_path)
        upsert_products(data, db_path)
        logger.info(f"Upsertrade {len(data)} rader till databasen")
        return len(data)
    except Exception as e:
        logger.exception("Fel i ETL-processen")
        raise

