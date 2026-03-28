from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from fastapi import FastAPI


DATABASE_URL = "mysql+pymysql://root:root@localhost/fastapi_db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
print('Database connection established.')