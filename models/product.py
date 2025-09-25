from sqlalchemy import Integer, String, Boolean, DateTime, DECIMAL, ForeignKey, BLOB, CheckConstraint, Index, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    product_code: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    product_variant: Mapped[str] = mapped_column(String(50), nullable=True)
    product_name: Mapped[str] = mapped_column(String(255), nullable=False)
    product_description: Mapped[str] = mapped_column(String(1000), default="")
    weight_volume: Mapped[str] = mapped_column(String(50), nullable=True)
    department_id: Mapped[int] = mapped_column(ForeignKey("supermarket_departments.id"), nullable=True)
    counter_id: Mapped[int] = mapped_column(ForeignKey("counter_departments.id"), nullable=True)
    supplier_id: Mapped[int] = mapped_column(ForeignKey("providers.id"), nullable=True)
    barcode: Mapped[str] = mapped_column(String(50), unique=True, nullable=True)
    plu_code: Mapped[str] = mapped_column(String(20), nullable=True)
    unit_of_measure: Mapped[str] = mapped_column(String(20), default="pcs")
    product_class: Mapped[str] = mapped_column(String(50), nullable=True)
    classification: Mapped[str] = mapped_column(String(100), nullable=True)
    checkout_method: Mapped[str] = mapped_column(String(20), nullable=True)
    consumption_flag: Mapped[str] = mapped_column(String(20), nullable=True)
    target_margin: Mapped[DECIMAL] = mapped_column(DECIMAL(5,2), nullable=True)
    selling_price: Mapped[DECIMAL] = mapped_column(DECIMAL(10,2), nullable=True)
    labeling_requirements: Mapped[str] = mapped_column(String(500), nullable=True)
    photo_data: Mapped[bytes] = mapped_column(BLOB, nullable=True)
    photo_filename: Mapped[str] = mapped_column(String(255), nullable=True)
    photo_mime_type: Mapped[str] = mapped_column(String(50), nullable=True)
    photo_size: Mapped[int] = mapped_column(Integer, nullable=True)
    sva_sale_active: Mapped[bool] = mapped_column(Boolean, default=False)
    sva_max_quantity: Mapped[int] = mapped_column(Integer, nullable=True)
    sva_loyalty_required: Mapped[bool] = mapped_column(Boolean, default=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.current_timestamp())
    updated_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.current_timestamp())

    department: Mapped["SupermarketDepartment"] = relationship("SupermarketDepartment", back_populates="products")
    counter: Mapped["CounterDepartment"] = relationship("CounterDepartment")
    supplier: Mapped["Provider"] = relationship("Provider", back_populates="products")

    __table_args__ = (
        CheckConstraint(
            "checkout_method IS NULL OR checkout_method IN ('BARCODE','SCALE','MANUAL')",
            name="checkout_method_check"
        ),
    )

    def __repr__(self) -> str:
        return f"<Product(code='{self.product_code}', name='{self.product_name}')>"


Index("idx_products_code", Product.product_code)
Index("idx_products_barcode", Product.barcode)
Index("idx_products_department_counter", Product.department_id, Product.counter_id)
