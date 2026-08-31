from sqlalchemy import Column, Integer, String, Float, Date
from app.core.database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    supplier = Column(String, nullable=False)
    manufacturing_date = Column(Date, nullable=False)
    expiry_date = Column(Date, nullable=False)
    quantity = Column(Float, nullable=False)  # kg or Liters
    unit_price = Column(Float, nullable=False)
    freshness_score = Column(Float, default=100.0)