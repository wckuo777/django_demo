from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 資料庫路徑 (sqlite db)
DATABASE_URL = "sqlite:///./fruits.db"

# 建立資料庫引擎
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# 建立 SessionLocal 類別
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 建立 Base 類別
Base = declarative_base()

# 定義 Fruits 表格
class Fruit(Base):
    __tablename__ = "fruits"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    color = Column(String)
