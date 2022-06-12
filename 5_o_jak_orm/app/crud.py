from sqlalchemy import func
from sqlalchemy.orm import Session

from . import models
from . import schemas


def get_shippers(db: Session):
    return db.query(models.Shipper).all()


def get_shipper(db: Session, shipper_id: int):
    return (
        db.query(models.Shipper).filter(models.Shipper.ShipperID == shipper_id).first()
    )


# task 5.1


def get_suppliers(db: Session):
    return db.query(models.Supplier).all()


def get_supplier(db: Session, supplier_id: int):
    return (
        db.query(models.Supplier)
        .filter(models.Supplier.SupplierID == supplier_id)
        .first()
    )


# task 5.2


def get_supplier_products(db: Session, supplier_id: int):
    return (
        db.query(
            models.Product.ProductID,
            models.Product.ProductName,
            models.Category.CategoryID,
            models.Category.CategoryName,
            models.Product.Discontinued,
        )
        .join(models.Supplier, models.Product.SupplierID == models.Supplier.SupplierID)
        .join(models.Category, models.Product.CategoryID == models.Category.CategoryID)
        .filter(models.Product.SupplierID == supplier_id)
        .order_by(models.Product.ProductID.desc())
        .all()
    )


# task 5.3
def create_supplier(db: Session, new_supplier: schemas.NewSupplier):
    highest_id = db.query(func.max(models.Supplier.SupplierID)).scalar()
    new_supplier.SupplierID = highest_id + 1
    db.add(models.Supplier(**new_supplier.dict()))
    db.commit()
    return get_supplier(db, highest_id + 1)
