from sqlalchemy import Column,Integer, String
from db.database import Base

class Factura(Base):
	__tablename__ = 'factura';
	id = Column(Integer, primary_key = True, index = True)