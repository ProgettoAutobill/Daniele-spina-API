from sqlalchemy.orm import Session
from models import StockMovementItem
from typing import cast, Optional


class StockMovementItemRepository:

    @staticmethod
    def create(session: Session, item: StockMovementItem):
        with session.begin():
            session.add(item)
            session.flush()
            session.refresh(item)
        return item

    @staticmethod
    def get_by_id(session: Session, item_id: int):
        item = cast(Optional[StockMovementItem], session.get(StockMovementItem, item_id))
        return item

    @staticmethod
    def get_all(session: Session):
        return session.query(StockMovementItem).all()

    @staticmethod
    def get_by_stock_movement(session: Session, stock_movement_id: int):
        return session.query(StockMovementItem).filter(
            StockMovementItem.stock_movement_id == stock_movement_id
        ).all()

    @staticmethod
    def update(session: Session, item_id: int, **kwargs):
        with session.begin():
            item = cast(Optional[StockMovementItem], session.get(StockMovementItem, item_id))
            if not item:
                return None
            for key, value in kwargs.items():
                if hasattr(item, key):
                    setattr(item, key, value)
            session.flush()
            session.refresh(item)
        return item

    @staticmethod
    def delete(session: Session, item_id: int):
        with session.begin():
            item = cast(Optional[StockMovementItem], session.get(StockMovementItem, item_id))
            if not item:
                return False
            session.delete(item)
        return True
