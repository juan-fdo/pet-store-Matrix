from pydantic import BaseModel
from datetime import date

class Base(BaseModel):
	pass

class Create(Base):
	pass

class SFactura(Base):
	fecha: date
	id: int
	class Config:
		orm_mode = True