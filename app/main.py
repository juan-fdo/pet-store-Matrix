from fastapi import Depends, FastAPI
from db.database import Base, engine, SessionLocal
from crud import CProducto, CFactura
from schemas import SProducto, SFactura, SFacturaDetalle
from sqlalchemy.orm import Session

app=FastAPI()
Base.metadata.create_all(bind = engine)

def get_db():
	db=SessionLocal()
	try:
		yield db
	finally:
		db.close()

@app.post("/productos/",response_model = SProducto.SProducto)
def create_producto(producto: SProducto.Create, db: Session = Depends(get_db)):
	return CProducto.create(db = db, producto = producto)

@app.get("/productos/{id}",response_model = SProducto.SProducto)
def get_producto(id: int, db: Session = Depends(get_db)):
	return CProducto.get(db, id = id)

@app.delete("/productos/{id}",response_model = SProducto.SProducto)
def delete_producto(id: int, db: Session = Depends(get_db)):
	return CProducto.delete(db, id = id)

@app.put("/productos/",response_model = SProducto.SProducto)
def update_producto(producto: SProducto.SProducto, db: Session = Depends(get_db)):
	return CProducto.update(db, producto)
	
@app.post("/facturas/",response_model = SFactura.SFactura)
def create_factura(factura: SFactura.Create, db: Session = Depends(get_db)):
	return CFactura.create(db = db, factura = factura)

@app.get("/facturas/{id}",response_model = SFactura.SFactura)
def get_factura(id: int, db: Session = Depends(get_db)):
	return CFactura.get(db, id = id)

@app.delete("/facturas/{id}",response_model = SFactura.SFactura)
def delete_factura(id: int, db: Session = Depends(get_db)):
	return CFactura.delete(db, id = id)


@app.post("/facturadetalles/",response_model = SFacturaDetalle.SFacturaDetalle)
def create_facturaDetalle(facturaDetalle: SFacturaDetalle.Create, db: Session = Depends(get_db)):
	return CFacturaDetalle.create(db = db, facturaDetalle = facturaDetalle)

@app.get("/facturadetalles/{id}",response_model = SFacturaDetalle.SFacturaDetalle)
def get_facturaDetalle(id: int, db: Session = Depends(get_db)):
	return CFacturaDetalle.get(db, id = id)

@app.delete("/facturadetalles/{id}",response_model = SFacturaDetalle.SFacturaDetalle)
def delete_facturaDetalle(id: int, db: Session = Depends(get_db)):
	return CFacturaDetalle.delete(db, id = id)

@app.put("/facturadetalles/",response_model = SFacturaDetalle.SFacturaDetalle)
def update_facturaDetalle(facturaDetalle: SFacturaDetalle.SFacturaDetalle, db: Session = Depends(get_db)):
	return CFacturaDetalle.update(db, facturaDetalle)
