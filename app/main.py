from fastapi import Depends, FastAPI
from db.database import Base, engine, SessionLocal
from db import crud, schemas
from sqlalchemy.orm import Session

app=FastAPI()
Base.metadata.create_all(bind = engine)

def get_db():
	db=SessionLocal()
	try:
		yield db
	finally:
		db.close()

@app.post("/productos/",response_model = schemas.Producto)
def create_producto(producto:schemas.ProductoCreate, db:Session = Depends(get_db)):
	return crud.create_producto(db = db, producto = producto)
