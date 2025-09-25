from fastapi import APIRouter, Query
from starlette import status

from metadata.apiDocs import api_docs
from metadata.erpDocs import erp_connect_desc, erp_connect_params, erp_connect_response
from schemas.request.erpRequest import ErpConnectRequest
from schemas.response.erpResponse import ErpConnectResponse, AccountingRecord, ErpAccountingImportResponse

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
    summary="Importa dati contabili dal gestionale"
)
async def import_accounting_data(
        data_type: str = Query(..., description="Tipo di dati (fatture, ordini, pagamenti)"),
        start_date: str = Query(..., description="Data di inizio periodo"),
        end_date: str = Query(..., description="Data di fine periodo")
):
    # Mock dei dati importati
    mock_records = [
        AccountingRecord(id="F001", amount=1000.0, date=start_date, description="Fattura cliente A"),
        AccountingRecord(id="F002", amount=500.0, date=start_date, description="Fattura cliente B"),
        AccountingRecord(id="F003", amount=300.0, date=start_date, description="Pagamento ordine C")
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
