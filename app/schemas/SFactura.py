from pydantic import BaseModel

class Base(BaseModel):
	pass

class Create(Base):
	pass

class SFactura(Base):
	id: int
	class Config:
		orm_mode = True