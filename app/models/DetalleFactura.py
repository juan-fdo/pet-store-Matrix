from sqlalchemy import Column,Integer,String
from db.database import Base

class DetalleFactura(Base):
	__tablename__ = 'detallefactura';
	id = Column(Integer, primary_key = True, index = True)
	factura_id = Column(Integer)
	producto_id = Column(Integer)
	cantidad = Column(Integer)