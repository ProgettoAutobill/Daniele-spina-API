
from sqlalchemy import create_engine, text, MetaData
from sqlalchemy.orm import sessionmaker
import os
from models import AccessLog,AdministrativeExpense,Authentication,Base,BaseProduct,BusinessEntity,Card,CashFlowEntry,ClickCollectRevenue,Client,Collaborator,CollaboratorContract,Employee,EmployeeContract,Expense,FacilityExpense,Finance,FinanceExpense,GoodsTransaction,GoodsTransactionProduct,GroceryProduct,Location,Lot,MarketingExpense,NonGroceryProduct,OnlineRevenue,Order,OtherExpense,OtherRevenue,Product,Provider,PurchaseExpense,ReturnExpense,Revenue,Role,SaleRevenue,ScaleProduct,ServiceRevenue,SingleProduct,StaffExpense,Stakeholder,StateEntity,Supplier,TaxExpense,TaxModel,UserBase,UtilityExpense

DATABASE_URL = f"postgresql://{os.getenv('DB_USER', 'admin')}:{os.getenv('DB_PASSWORD', 'password123')}@{os.getenv('DB_HOST', 'localhost')}:{os.getenv('DB_PORT', '5432')}/{os.getenv('DB_NAME', 'sistema_gestionale')}"

try:
    engine = create_engine(DATABASE_URL, echo=True)
    SessionLocal = sessionmaker(bind=engine)
    print("Connecting to PostgreSQL database in Docker...")
    # Test connessione
    with engine.connect() as connection:
        result = connection.execute(text("SELECT version()"))
        print(f"Connected successfully! PostgreSQL version: {result.fetchone()[0]}")
    print("\nCreating all tables...")
    Base.metadata.create_all(bind=engine)
    metadata = MetaData()
    metadata.reflect(bind=engine)
    print(f"\nDatabase '{DATABASE_URL.split('/')[-1]}' created successfully!")
    print(f"Total tables created: {len(metadata.tables)}")
    for table_name in sorted(metadata.tables.keys()):
        table = metadata.tables[table_name]
        print(f"  • {table_name} ({len(table.columns)} columns)")
    print("\nDatabase is ready for use!")
    print(f"Connection string: {DATABASE_URL}")

except Exception as e:
    print(f"Error creating database: {e}")
