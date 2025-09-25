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

