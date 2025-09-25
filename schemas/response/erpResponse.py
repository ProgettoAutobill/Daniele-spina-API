from pydantic import BaseModel, Field
from typing import List, Optional


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


class ErpEntityRecord(BaseModel):
    entityId: str
    name: str
    entityType: str
    status: str
    outstandingPayments: float


class ErpEntityImportResponse(BaseModel):
    importedRecords: List[ErpEntityRecord] = Field(..., alias="importedRecords")
    totalRecords: int = Field(..., alias="totalRecords")
    totalOutstanding: float = Field(..., alias="totalOutstanding")
    message: str


class ErpSyncLogEntry(BaseModel):
    timestamp: str
    message: str


class ErpSyncStatusRecord(BaseModel):
    syncId: str
    status: str
    startedAt: str
    completedAt: Optional[str] = None
    logs: List[ErpSyncLogEntry]


class ErpSyncStatusResponse(BaseModel):
    syncRecords: List[ErpSyncStatusRecord] = Field(..., alias="syncRecords")
    totalRecords: int = Field(..., alias="totalRecords")
    message: str
