from sqlalchemy import Column,Integer,String
from db.database import Base
class Producto(Base):
	__tablename__ = 'producto';
	id = Column(Integer, primary_key = True, index = True)
	nombre = Column(String)
	precio = Column(Integer)