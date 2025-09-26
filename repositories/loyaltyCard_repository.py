from sqlalchemy.orm import Session
from models import LoyaltyCard
from typing import cast, Optional


class LoyaltyCardRepository:

    @staticmethod
    def create(session: Session, loyalty_card: LoyaltyCard):
        with session.begin():
            session.add(loyalty_card)
            session.flush()
            session.refresh(loyalty_card)
        return loyalty_card

    @staticmethod
    def get_by_id(session: Session, card_id: int):
        loyalty_card = cast(Optional[LoyaltyCard], session.get(LoyaltyCard, card_id))
        return loyalty_card

    @staticmethod
    def get_all(session: Session):
        return session.query(LoyaltyCard).all()

    @staticmethod
    def get_by_client(session: Session, client_id: int):
        return session.query(LoyaltyCard).filter(LoyaltyCard.client_id == client_id).all()

    @staticmethod
    def get_active(session: Session):
        return session.query(LoyaltyCard).filter(LoyaltyCard.is_active == True).all()

    @staticmethod
    def update(session: Session, card_id: int, **kwargs):
        with session.begin():
            loyalty_card = cast(Optional[LoyaltyCard], session.get(LoyaltyCard, card_id))
            if not loyalty_card:
                return None
            for key, value in kwargs.items():
                if hasattr(loyalty_card, key):
                    setattr(loyalty_card, key, value)
            session.flush()
            session.refresh(loyalty_card)
        return loyalty_card

    @staticmethod
    def delete(session: Session, card_id: int):
        with session.begin():
            loyalty_card = cast(Optional[LoyaltyCard], session.get(LoyaltyCard, card_id))
            if not loyalty_card:
                return False
            session.delete(loyalty_card)
        return True
