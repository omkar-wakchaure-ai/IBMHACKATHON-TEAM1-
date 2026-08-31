from sqlalchemy import Column, Integer, String, Float, Date
from app.core.database import Base

class PurchaseOrder(Base):
    __tablename__ = "purchase_orders"

    id = Column(Integer, primary_key=True, index=True)
    po_number = Column(String, unique=True, index=True, nullable=False)
    generation_date = Column(Date, nullable=False)
    total_cost = Column(Float, nullable=False)
    pdf_file_path = Column(String, nullable=True)
    status = Column(String, default="Generated") # Generated, Approved, Sent