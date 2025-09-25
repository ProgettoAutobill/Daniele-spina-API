from typing import Optional

from fastapi import APIRouter, Query
from starlette import status

from metadata.apiDocs import api_docs
from metadata.erpDocs import erp_connect_desc, erp_connect_params, erp_connect_response, erp_accounting_desc, \
    erp_accounting_params, erp_accounting_response, erp_import_inventory_desc, erp_import_inventory_params, \
    erp_import_inventory_response
from schemas.request.erpRequest import ErpConnectRequest
from schemas.response.erpResponse import ErpConnectResponse, ErpAccountingImportResponse, \
    ErpAccountingRecord, ErpInventoryImportResponse, ErpInventoryRecord

router = APIRouter(
    prefix="/erp",
    tags=["erp"]
)


@router.post(
    "/connect",
    response_model=ErpConnectResponse,
    status_code=status.HTTP_200_OK,
    **api_docs(erp_connect_desc, erp_connect_params, erp_connect_response)
)
async def connect(request: ErpConnectRequest):
    # Dati mockati
    if request.erpType.lower() in ["sap", "oracle", "zucchetti"]:
        response = ErpConnectResponse(
            status="success",
            message=f"Connessione a {request.erpType} stabilita con successo.",
            authToken="mocked_token_123456"
        )
    else:
        response = ErpConnectResponse(
            status="failure",
            message=f"ERP type {request.erpType} non supportato.",
            authToken=None
        )
    return response


@router.get(
    "/import/accounting",
    response_model=ErpAccountingImportResponse,
    status_code=status.HTTP_200_OK,
    **api_docs(erp_accounting_desc, erp_accounting_params, erp_accounting_response)
)
async def import_accounting_data(
        data_type: str = Query(..., description="Tipo di dati (fatture, ordini, pagamenti)"),
        start_date: str = Query(..., description="Data di inizio periodo"),
        end_date: str = Query(..., description="Data di fine periodo")
):
    # Mock dei dati importati
    mock_records = [
        ErpAccountingRecord(id="F001", amount=1000.0, date=start_date, description="Fattura cliente A"),
        ErpAccountingRecord(id="F002", amount=500.0, date=start_date, description="Fattura cliente B"),
        ErpAccountingRecord(id="F003", amount=300.0, date=start_date, description="Pagamento ordine C")
    ]

    total_amount = sum(record.amount for record in mock_records)
    total_records = len(mock_records)

    response = ErpAccountingImportResponse(
        importedRecords=mock_records,
        totalRecords=total_records,
        totalAmount=total_amount,
        message=f"Importati {total_records} record di tipo {data_type} dal {start_date} al {end_date}."
    )
    return response


@router.get(
    "/import/inventory",
    response_model=ErpInventoryImportResponse,
    status_code=status.HTTP_200_OK,
    **api_docs(erp_import_inventory_desc, erp_import_inventory_params, erp_import_inventory_response)
)
async def import_inventory_data(
        warehouse_id: Optional[str] = Query(None, description="ID del magazzino (opzionale)"),
        product_category: Optional[str] = Query(None, description="Categoria di prodotti (opzionale)")
):
    # Dati mockati
    mock_inventory = [
        ErpInventoryRecord(productId="P001", name="Latte", category="Bevande", warehouseId="W001", quantity=50),
        ErpInventoryRecord(productId="P002", name="Pane", category="Alimenti", warehouseId="W002", quantity=100),
        ErpInventoryRecord(productId="P003", name="Uova", category="Alimenti", warehouseId="W001", quantity=200),
        ErpInventoryRecord(productId="P004", name="Detersivo", category="Pulizia", warehouseId="W003", quantity=75)
    ]

    # Filtra in base ai parametri opzionali
    filtered_inventory = [
        record for record in mock_inventory
        if (warehouse_id is None or record.warehouseId == warehouse_id) and
           (product_category is None or record.category == product_category)
    ]

    response = ErpInventoryImportResponse(
        importedRecords=filtered_inventory,
        totalRecords=len(filtered_inventory),
        message=f"Importati {len(filtered_inventory)} record di inventario."
    )
    return response
