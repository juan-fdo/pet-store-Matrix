from sqlalchemy.orm import Session
from schemas import SFactura
from models.Factura import Factura
from datetime import date

def create(db: Session, factura: SFactura.Create):
	db_factura = Factura(fecha = date.today())
	db.add(db_factura)
	db.commit()
	db.refresh(db_factura)
	return db_factura

def get(db: Session, id: int):
	return db.query(Factura).filter(Factura.id == id).first()
	
def delete(db: Session, id: int):
	db_factura = get(db = db, id = id)
	db.delete(db_factura)
	db.commit()
	return db_factura

