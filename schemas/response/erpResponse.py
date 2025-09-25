from pydantic import BaseModel, Field
from typing import List


class ErpConnectResponse(BaseModel):
    status: str
    message: str
    authToken: str = None


class AccountingRecord(BaseModel):
    id: str
    amount: float
    date: str
    description: str


class ErpAccountingImportResponse(BaseModel):
    importedRecords: List[AccountingRecord] = Field(..., alias="importedRecords")
    totalRecords: int = Field(..., alias="totalRecords")
    totalAmount: float = Field(..., alias="totalAmount")
    message: str