import pandas as pd
from sqlalchemy import create_engine

from services import load_data
  # your function

DATABASE_URL = "mysql+pymysql://root:root@localhost/fastapi_db"

engine = create_engine(DATABASE_URL)

df =load_data()

df.rename(columns={"student_id": "id"}, inplace=True)

df.to_sql("students", con=engine, if_exists="replace", index=False)

print("✅ Data inserted into MySQL")