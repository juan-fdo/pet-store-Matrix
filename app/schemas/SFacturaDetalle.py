from pydantic import BaseModel

class Base(BaseModel):
	factura_id: int
	producto_id: int
	cantidad: int

class Create(Base):
	pass

class SFacturaDetalle(Base):
	id: int
	class Config:
		orm_mode = True