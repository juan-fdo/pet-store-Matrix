from sqlalchemy.orm import Session
from schemas import SProducto
from models.Producto import Producto

def create(db: Session, producto: SProducto.Create):
	db_producto = Producto(nombre = producto.nombre, precio = producto.precio)
	db.add(db_producto)
	db.commit()
	db.refresh(db_producto)
	return db_producto

def get(db: Session, id: int):
	return db.query(Producto).filter(Producto.id == id).first()

def delete(db: Session, id: int):
	db_producto = get(db = db,id = id)
	db.delete(db_producto)
	db.commit()
	return db_producto
