from sqlalchemy.orm import Session
from models import Product
from typing import cast, Optional


class ProductRepository:

    @staticmethod
    def create(session: Session, product: Product):
        with session.begin():
            session.add(product)
            session.flush()
            session.refresh(product)
        return product

    @staticmethod
    def get_by_id(session: Session, product_id: int):
        product = cast(Optional[Product], session.get(Product, product_id))
        return product

    @staticmethod
    def get_all(session: Session):
        return session.query(Product).all()

    @staticmethod
    def get_by_code(session: Session, product_code: str):
        return session.query(Product).filter(Product.product_code == product_code).all()

    @staticmethod
    def get_by_barcode(session: Session, barcode: str):
        return session.query(Product).filter(Product.barcode == barcode).all()

    @staticmethod
    def get_active(session: Session):
        return session.query(Product).filter(Product.is_active == True).all()

    @staticmethod
    def update(session: Session, product_id: int, **kwargs):
        with session.begin():
            product = cast(Optional[Product], session.get(Product, product_id))
            if not product:
                return None
            for key, value in kwargs.items():
                if hasattr(product, key):
                    setattr(product, key, value)
            session.flush()
            session.refresh(product)
        return product

    @staticmethod
    def delete(session: Session, product_id: int):
        with session.begin():
            product = cast(Optional[Product], session.get(Product, product_id))
            if not product:
                return False
            session.delete(product)
        return True
