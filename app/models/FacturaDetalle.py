from sqlalchemy import Column,Integer,String
from db.database import Base

class FacturaDetalle(Base):
	__tablename__ = 'facturadetalle';
	id = Column(Integer, primary_key = True, index = True)
	factura_id = Column(Integer)
	producto_id = Column(Integer)
	cantidad = Column(Integer)