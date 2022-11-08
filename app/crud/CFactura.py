from sqlalchemy.orm import Session
from schemas import SFactura
from models.Factura import Factura

def create(db: Session, factura: SFactura.Create):
	db_factura = Factura()
	db.add(db_factura)
	db.commit()
	db.refresh(db_factura)
	return db_factura

def get(db: Session, id: int):
	return db.query(Factura).filter(Factura.id == id).first()