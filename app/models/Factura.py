from sqlalchemy import Column,Integer, String, Date
from db.database import Base
from datetime import date
class Factura(Base):
	__tablename__ = 'factura';
	id = Column(Integer, primary_key = True, index = True)
	fecha = Column(Date)