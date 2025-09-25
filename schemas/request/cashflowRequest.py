from typing import List
from pydantic import BaseModel


class AccountingRecord(BaseModel):
    id: str
    amount: float
    date: str
    description: str


class AccountingDataRequest(BaseModel):
    dataType: str
    data: List[AccountingRecord]

