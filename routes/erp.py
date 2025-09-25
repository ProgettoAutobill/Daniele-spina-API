from typing import Optional

from fastapi import APIRouter, Query
from starlette import status

from metadata.apiDocs import api_docs
from metadata.erpDocs import erp_connect_desc, erp_connect_params, erp_connect_response, erp_accounting_desc, \
    erp_accounting_params, erp_accounting_response, erp_import_inventory_desc, erp_import_inventory_params, \
    erp_import_inventory_response, erp_sync_desc, erp_sync_params, erp_sync_response, erp_mapping_desc, \
    erp_mapping_params, erp_mapping_response, erp_import_entities_desc, erp_import_entities_params, \
    erp_import_entities_response, erp_sync_status_desc, erp_sync_status_params, erp_sync_status_response
from schemas.request.erpRequest import ErpConnectRequest, ErpSyncRequest, ErpMappingRequest
from schemas.response.erpResponse import ErpConnectResponse, ErpAccountingImportResponse, \
    ErpAccountingRecord, ErpInventoryImportResponse, ErpInventoryRecord, ErpSyncResponse, ErpModuleSyncResult, \
    ErpMappingResponse, ErpEntityImportResponse, ErpEntityRecord, ErpSyncStatusRecord, ErpSyncLogEntry, \
    ErpSyncStatusResponse

router = APIRouter(
    prefix="/api/erp",
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


@router.post(
    "/sync",
    response_model=ErpSyncResponse,
    status_code=status.HTTP_200_OK,
    **api_docs(erp_sync_desc, erp_sync_params, erp_sync_response)
)
async def sync_data(request: ErpSyncRequest):
    # Dati Mockati
    mock_results = []
    for module in request.dataModules:
        mock_results.append(
            ErpModuleSyncResult(
                moduleName=module,
                status="success",
                recordsSynced=10
            )
        )

    response = ErpSyncResponse(
        results=mock_results,
        totalModules=len(request.dataModules),
        message=f"Sincronizzati {len(request.dataModules)} moduli in {request.syncDirection} mode."
    )
    return response


@router.put(
    "/mapping",
    response_model=ErpMappingResponse,
    status_code=status.HTTP_200_OK,
    **api_docs(erp_mapping_desc, erp_mapping_params, erp_mapping_response)
)
async def configure_mapping(request: ErpMappingRequest):
    # Dati mockati
    if request.fieldMappings:
        response = ErpMappingResponse(
            status="success",
            message=f"Mappatura per {request.entityType} su {request.erpType} configurata con successo."
        )
    else:
        response = ErpMappingResponse(
            status="failure",
            message=f"Nessuna mappatura fornita per {request.entityType} su {request.erpType}."
        )
    return response


@router.get(
    "/import/entities",
    response_model=ErpEntityImportResponse,
    status_code=status.HTTP_200_OK,
    **api_docs(erp_import_entities_desc, erp_import_entities_params, erp_import_entities_response)
)
async def import_entities(
        entity_type: str = Query(..., description="Tipo di entità (cliente, fornitore)", alias="entityType"),
        status: Optional[str] = Query(None, description="Stato (attivo, inattivo)")
):
    # Dati mockati
    mock_entities = [
        ErpEntityRecord(entityId="C001", name="Mario Rossi", entityType="cliente", status="attivo",
                     outstandingPayments=500.0),
        ErpEntityRecord(entityId="C002", name="Luca Bianchi", entityType="cliente", status="inattivo",
                     outstandingPayments=0.0),
        ErpEntityRecord(entityId="F001", name="Fornitore XYZ", entityType="fornitore", status="attivo",
                     outstandingPayments=1200.0),
        ErpEntityRecord(entityId="F002", name="Fornitore ABC", entityType="fornitore", status="inattivo",
                     outstandingPayments=0.0)
    ]

    # Filtra in base ai parametri
    filtered_entities = [
        entity for entity in mock_entities
        if entity.entityType == entity_type and (status is None or entity.status == status)
    ]

    total_outstanding = sum(entity.outstandingPayments for entity in filtered_entities)

    response = ErpEntityImportResponse(
        importedRecords=filtered_entities,
        totalRecords=len(filtered_entities),
        totalOutstanding=total_outstanding,
        message=f"Importati {len(filtered_entities)} record di tipo {entity_type}."
    )
    return response



@router.get(
    "/sync/status",
    response_model=ErpSyncStatusResponse,
    status_code=status.HTTP_200_OK,
    **api_docs(erp_sync_status_desc, erp_sync_status_params, erp_sync_status_response)
)
async def monitor_sync_status(
        sync_id: Optional[str] = Query(None, description="ID della sincronizzazione (opzionale)", alias="syncId"),
        status_filter: Optional[str] = Query(None, alias="status",
                                             description="Filtra per stato (in corso, completato, fallito)")
):
    # Dati mockati
    mock_syncs = [
        ErpSyncStatusRecord(
            syncId="SYNC001",
            status="completato",
            startedAt="2025-09-25T10:00:00",
            completedAt="2025-09-25T10:05:00",
            logs=[
                ErpSyncLogEntry(timestamp="2025-09-25T10:01:00", message="Inizio import fatture"),
                ErpSyncLogEntry(timestamp="2025-09-25T10:03:00", message="Import ordini completato"),
            ]
        ),
        ErpSyncStatusRecord(
            syncId="SYNC002",
            status="in corso",
            startedAt="2025-09-25T11:00:00",
            logs=[
                ErpSyncLogEntry(timestamp="2025-09-25T11:01:00", message="Avvio sincronizzazione inventario")
            ]
        ),
        ErpSyncStatusRecord(
            syncId="SYNC003",
            status="fallito",
            startedAt="2025-09-25T09:00:00",
            completedAt="2025-09-25T09:02:00",
            logs=[
                ErpSyncLogEntry(timestamp="2025-09-25T09:01:00", message="Errore connessione ERP")
            ]
        )
    ]

    # Filtra per sync_id e status
    filtered_syncs = [
        record for record in mock_syncs
        if (sync_id is None or record.syncId == sync_id) and
           (status_filter is None or record.status == status_filter)
    ]

    response = ErpSyncStatusResponse(
        syncRecords=filtered_syncs,
        totalRecords=len(filtered_syncs),
        message=f"Trovati {len(filtered_syncs)} record di sincronizzazione."
    )

    return response