from pydantic import BaseModel, Field
from typing import List


class ErpConnectResponse(BaseModel):
    status: str
    message: str
    authToken: str = None


class ErpAccountingRecord(BaseModel):
    id: str
    amount: float
    date: str
    description: str


class ErpAccountingImportResponse(BaseModel):
    importedRecords: List[ErpAccountingRecord] = Field(..., alias="importedRecords")
    totalRecords: int = Field(..., alias="totalRecords")
    totalAmount: float = Field(..., alias="totalAmount")
    message: str


class ErpInventoryRecord(BaseModel):
    productId: str
    name: str
    category: str
    warehouseId: str
    quantity: int


class ErpInventoryImportResponse(BaseModel):
    importedRecords: List[ErpInventoryRecord] = Field(..., alias="importedRecords")
    totalRecords: int = Field(..., alias="totalRecords")
    message: str


class ErpModuleSyncResult(BaseModel):
    moduleName: str
    status: str
    recordsSynced: int


class ErpSyncResponse(BaseModel):
    results: List[ErpModuleSyncResult] = Field(..., alias="results")
    totalModules: int = Field(..., alias="totalModules")
    message: str


class ErpMappingResponse(BaseModel):
    status: str
    message: str
