from pydantic import BaseModel

class Base(BaseModel):
	producto_id: id
	cantidad: int

class Create(Base):
	pass

class SFacturaDetalle(Base):
	id: int
	factura_id: int
	class Config:
		orm_mode = True