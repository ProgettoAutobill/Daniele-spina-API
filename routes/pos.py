from typing import Optional
from fastapi import APIRouter, Query
from starlette import status

from metadata.apiDocs import api_docs
from metadata.posDocs import pos_connect_params, pos_connect_desc, pos_connect_response, pos_transactions_desc, \
    pos_transactions_params, pos_transactions_response
from schemas.request.posRequest import PosConnectRequest
from schemas.response.posResponse import PosConnectResponse, PosTransactionImportResponse, PosTransactionRecord

router = APIRouter(
    prefix="/pos",
    tags=["pos"]
)


@router.post(
    "/connect",
    response_model=PosConnectResponse,
    status_code=status.HTTP_200_OK,
    **api_docs(pos_connect_desc, pos_connect_params, pos_connect_response)
)
async def connect_pos(request: PosConnectRequest):
    # Dati mockati
    supported_pos = ["pos n1", "pos n2", "pos n3"]

    if request.posType in supported_pos:
        response = PosConnectResponse(
            status="success",
            message=f"Connessione a {request.posType} per lo store {request.storeId} stabilita con successo.",
            authToken="mocked_pos_token_123456"
        )
    else:
        response = PosConnectResponse(
            status="failure",
            message=f"POS type {request.posType} non supportato.",
            authToken=None
        )
    return response


@router.get(
    "/transactions",
    response_model=PosTransactionImportResponse,
    status_code=status.HTTP_200_OK,
    ** api_docs(pos_transactions_desc, pos_transactions_params, pos_transactions_response)
)
async def import_transactions(
        start_date: str = Query(..., description="Data di inizio periodo"),
        end_date: str = Query(..., description="Data di fine periodo"),
        transaction_type: Optional[str] = Query(None, description="Tipo di transazione (vendita, reso, ecc.)")
):
    # Dati mockati
    mock_transactions = [
        PosTransactionRecord(transactionId="T001", date=start_date, transactionType="vendita", amount=100.0,
                          storeId="STORE001"),
        PosTransactionRecord(transactionId="T002", date=start_date, transactionType="vendita", amount=50.0,
                          storeId="STORE001"),
        PosTransactionRecord(transactionId="T003", date=start_date, transactionType="reso", amount=-20.0,
                          storeId="STORE002")
    ]

    # Filtra per tipo di transazione se specificato
    filtered_transactions = [
        tx for tx in mock_transactions
        if transaction_type is None or tx.transactionType == transaction_type
    ]

    total_amount = sum(tx.amount for tx in filtered_transactions)

    response = PosTransactionImportResponse(
        importedTransactions=filtered_transactions,
        totalTransactions=len(filtered_transactions),
        totalAmount=total_amount,
        message=f"Importate {len(filtered_transactions)} transazioni dal {start_date} al {end_date}."
    )
    return response

