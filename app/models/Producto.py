class Producto(Base):
	__tablename__ = 'producto';
	id = Column(Integer, primary_key = True, index = True)
	name = Column(String)