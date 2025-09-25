from pydantic import BaseModel, Field
from typing import List, Optional


class PosConnectResponse(BaseModel):
    status: str
    message: str
    authToken: Optional[str] = None


class PosTransactionRecord(BaseModel):
    transactionId: str
    date: str
    transactionType: str
    amount: float
    storeId: str


class PosTransactionImportResponse(BaseModel):
    importedTransactions: List[PosTransactionRecord] = Field(..., alias="importedTransactions")
    totalTransactions: int = Field(..., alias="totalTransactions")
    totalAmount: float = Field(..., alias="totalAmount")
    message: str


class PosProductSyncResult(BaseModel):
    categoryName: str
    status: str
    productsSynced: int


class PosProductSyncResponse(BaseModel):
    results: List[PosProductSyncResult] = Field(..., alias="results")
    totalCategories: int = Field(..., alias="totalCategories")
    message: str


class PosSalesTrendEntry(BaseModel):
    date: str
    totalSales: float
    transactions: int


class PosSalesAnalysisResponse(BaseModel):
    storeId: Optional[str] = None
    productCategory: Optional[str] = None
    timeframe: str
    totalSales: float
    totalTransactions: int
    trend: List[PosSalesTrendEntry]
    message: str

