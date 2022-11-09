from pydantic import BaseModel

class Base(BaseModel):
	nombre: str
	precio: int

class Create(Base):
	pass

class SProducto(Base):
	id: int
	class Config:
		orm_mode = True
