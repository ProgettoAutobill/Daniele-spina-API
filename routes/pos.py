from typing import Optional
from fastapi import APIRouter, Query
from starlette import status

from metadata.apiDocs import api_docs
from metadata.posDocs import pos_connect_params, pos_connect_desc, pos_connect_response, pos_transactions_desc, \
    pos_transactions_params, pos_transactions_response, pos_products_sync_desc, pos_products_sync_params, \
    pos_products_sync_response, pos_sales_analysis_desc, pos_sales_analysis_params, pos_sales_analysis_response
from schemas.request.posRequest import PosConnectRequest, PosProductSyncRequest
from schemas.response.posResponse import PosConnectResponse, PosTransactionImportResponse, PosTransactionRecord, \
    PosProductSyncResponse, PosProductSyncResult, PosSalesTrendEntry, PosSalesAnalysisResponse

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


@router.post(
    "/products/sync",
    response_model=PosProductSyncResponse,
    status_code=status.HTTP_200_OK,
    ** api_docs(pos_products_sync_desc, pos_products_sync_params, pos_products_sync_response)
)
async def sync_products(request: PosProductSyncRequest):
    # Dati mockati
    mock_results = [
        PosProductSyncResult(
            categoryName=category,
            status="success",
            productsSynced=10
        ) for category in request.productCategories
    ]

    response = PosProductSyncResponse(
        results=mock_results,
        totalCategories=len(request.productCategories),
        message=f"Sincronizzate {len(request.productCategories)} categorie di prodotti in {request.syncDirection} mode."
    )
    return response


@router.get(
    "/sales/analysis",
    response_model=PosSalesAnalysisResponse,
    status_code=status.HTTP_200_OK,
    ** api_docs(pos_sales_analysis_desc, pos_sales_analysis_params, pos_sales_analysis_response)
)
async def analyze_sales(
        timeframe: str = Query(..., description="Periodo di analisi (giornaliero, settimanale, mensile)"),
        product_category: Optional[str] = Query(None, description="Categoria di prodotti (opzionale)"),
        store_id: Optional[str] = Query(None, description="ID del negozio (opzionale)")
):
    # Mock dei dati di trend
    mock_trend = [
        PosSalesTrendEntry(date="2025-09-21", totalSales=1000.0, transactions=25),
        PosSalesTrendEntry(date="2025-09-22", totalSales=1200.0, transactions=30),
        PosSalesTrendEntry(date="2025-09-23", totalSales=900.0, transactions=20),
        PosSalesTrendEntry(date="2025-09-24", totalSales=1500.0, transactions=35)
    ]

    total_sales = sum(entry.totalSales for entry in mock_trend)
    total_transactions = sum(entry.transactions for entry in mock_trend)

    response = PosSalesAnalysisResponse(
        storeId=store_id,
        productCategory=product_category,
        timeframe=timeframe,
        totalSales=total_sales,
        totalTransactions=total_transactions,
        trend=mock_trend,
        message=f"Analisi delle vendite completata per timeframe '{timeframe}'."
    )

    return response