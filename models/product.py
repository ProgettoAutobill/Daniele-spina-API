from datetime import datetime

from sqlalchemy import Integer, String, Boolean, DateTime, DECIMAL, ForeignKey, BLOB, CheckConstraint, Index, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    product_code: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    product_variant: Mapped[str] = mapped_column(String(50), default=None)
    product_name: Mapped[str] = mapped_column(String(255), nullable=False)
    product_description: Mapped[str] = mapped_column(String(1000), default="")
    weight_volume: Mapped[str] = mapped_column(String(50), default=None)
    department_id: Mapped[int] = mapped_column(Integer, ForeignKey("supermarket_departments.id"), default=None)
    counter_id: Mapped[int] = mapped_column(Integer, ForeignKey("counter_departments.id"), default=None)
    supplier_id: Mapped[int] = mapped_column(Integer, ForeignKey("providers.id"), default=None)
    barcode: Mapped[str] = mapped_column(String(50), unique=True, default=None)
    plu_code: Mapped[str] = mapped_column(String(20), default=None)
    unit_of_measure: Mapped[str] = mapped_column(String(20), default="pcs")
    product_class: Mapped[str] = mapped_column(String(50), default=None)
    classification: Mapped[str] = mapped_column(String(100), default=None)
    checkout_method: Mapped[str] = mapped_column(String(20), default=None)
    consumption_flag: Mapped[str] = mapped_column(String(20), default=None)
    target_margin: Mapped[DECIMAL] = mapped_column(DECIMAL(5,2), default=None)
    selling_price: Mapped[DECIMAL] = mapped_column(DECIMAL(10,2), default=None)
    labeling_requirements: Mapped[str] = mapped_column(String(500), default=None)
    photo_data: Mapped[bytes] = mapped_column(BLOB, default=None)
    photo_filename: Mapped[str] = mapped_column(String(255), default=None)
    photo_mime_type: Mapped[str] = mapped_column(String(50), default=None)
    photo_size: Mapped[int] = mapped_column(Integer, default=None)
    sva_sale_active: Mapped[bool] = mapped_column(Boolean, default=False)
    sva_max_quantity: Mapped[int] = mapped_column(Integer, default=None)
    sva_loyalty_required: Mapped[bool] = mapped_column(Boolean, default=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    department: Mapped["SupermarketDepartment"] = relationship("SupermarketDepartment", back_populates="products")
    counter: Mapped["CounterDepartment"] = relationship("CounterDepartment", back_populates="products")
    supplier: Mapped["Provider"] = relationship("Provider", back_populates="products")


Index("idx_products_code", Product.product_code)
Index("idx_products_barcode", Product.barcode)
Index("idx_products_department_counter", Product.department_id, Product.counter_id)