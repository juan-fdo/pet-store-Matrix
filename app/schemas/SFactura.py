from pydantic import BaseModel

class Base(BaseModel):
	datetime.date

class Create(Base):
	pass

class SFactura(Base):
	id: int
	class Config:
		orm_mode = True