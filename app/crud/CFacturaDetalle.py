from sqlalchemy.orm import Session
from schemas import SFacturaDetalle
from models.FacturaDetalle import FacturaDetalle

def create(db: Session, facturaDetalle: SFacturaDetalle.Create):
	db_facturaDetalle = FacturaDetalle()
	db.add(db_facturaDetalle)
	db.commit()
	db.refresh(db_facturaDetalle)
	return db_facturaDetalle

def get(db: Session, id: int):
	return db.query(FacturaDetalle).filter(FacturaDetalle.id == id).first()
	
def delete(db: Session, id: int):
	db_facturaDetalle = get(db = db, id = id)
	db.delete(db_facturaDetalle)
	db.commit()
	return db_facturaDetalle

def update(db: Session, facturaDetalle: SFacturaDetalle.SFacturaDetalle):
	db_facturaDetalle = get(db = db, id = facturaDetalle.id)
	db_facturaDetalle.producto_id = facturaDetalle.producto_id
	db_facturaDetalle.cantidad = facturaDetalle.cantidad
	db.commit()
	db.refresh(db_facturaDetalle)
	return db_facturaDetalle
