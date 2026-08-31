from sqlalchemy import Column, Integer, Float, Date, ForeignKey
from app.core.database import Base

class InventoryLog(Base):
    __tablename__ = "inventory_logs"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    date_recorded = Column(Date, nullable=False)
    stock_level = Column(Float, nullable=False)
    spoilage_risk_percentage = Column(Float, default=0.0)