from sqlalchemy import create_engine, inspect , text
from sqlalchemy.orm import sessionmaker, Session
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models import (
    Base, BusinessCost, BusinessRevenue, Client, CounterDepartment, Employee,
    EmployeeContract, FinancialCategory, KeycloakSession, Location, LoyaltyCard,
    Product, Provider, Role, StockMovement, StockMovementItem, SupermarketDepartment,
    User, UserPermission
)

DATABASE_URL = "sqlite:///./database/database.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def test_db_connection():
    try:
        with engine.connect() as conn:
            version = conn.execute(text("SELECT sqlite_version()")).fetchone()[0]
            print(f"Connected! SQLite version: {version}")

        inspector = inspect(engine)
        print(f"\nTables in dbsmartapi:")
        for table_name in inspector.get_table_names():
            print(f"  • {table_name}")

    except Exception as e:
        print(f"Database connection error: {e}")


if __name__ == "__main__":
    #init_db()
    test_db_connection()

