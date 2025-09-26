from sqlalchemy.orm import Session
from models import StockMovement
from typing import cast, Optional


class StockMovementRepository:

    @staticmethod
    def create(session: Session, stock_movement: StockMovement):
        with session.begin():
            session.add(stock_movement)
            session.flush()
            session.refresh(stock_movement)
        return stock_movement

    @staticmethod
    def get_by_id(session: Session, movement_id: int):
        stock_movement = cast(Optional[StockMovement], session.get(StockMovement, movement_id))
        return stock_movement

    @staticmethod
    def get_all(session: Session):
        return session.query(StockMovement).all()

    @staticmethod
    def get_by_number(session: Session, movement_number: str):
        return session.query(StockMovement).filter(StockMovement.movement_number == movement_number).all()

    @staticmethod
    def update(session: Session, movement_id: int, **kwargs):
        with session.begin():
            stock_movement = cast(Optional[StockMovement], session.get(StockMovement, movement_id))
            if not stock_movement:
                return None
            for key, value in kwargs.items():
                if hasattr(stock_movement, key):
                    setattr(stock_movement, key, value)
            session.flush()
            session.refresh(stock_movement)
        return stock_movement

    @staticmethod
    def delete(session: Session, movement_id: int):
        with session.begin():
            stock_movement = cast(Optional[StockMovement], session.get(StockMovement, movement_id))
            if not stock_movement:
                return False
            session.delete(stock_movement)
        return True
