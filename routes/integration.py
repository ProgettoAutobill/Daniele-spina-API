from fastapi import APIRouter, Query, status
from starlette import status
from metadata.apiDocs import api_docs
from metadata.integrationDocs import integration_correlate_desc, integration_correlate_params, \
    integration_correlate_response, integration_inventory_impact_desc, integration_inventory_impact_params, \
    integration_inventory_optimization_response
from schemas.request.integrationRequest import IntegrationCorrelationRequest
from schemas.response.integrationResponse import IntegrationCorrelationResponse, IntegrationCorrelationResult, \
    IntegrationInventoryImpactEntry, IntegrationInventoryImpactResponse

router = APIRouter(
    prefix="/integration",
    tags=["integration"]
)

@router.post(
    "/correlate",
    response_model=IntegrationCorrelationResponse,
    status_code=status.HTTP_200_OK,
    **api_docs(integration_correlate_desc, integration_correlate_params, integration_correlate_response)
)
async def correlate_data(request: IntegrationCorrelationRequest):
    # Dati mockati
    mock_results = [
        IntegrationCorrelationResult(
            dataSourcePair=f"{request.correlationType}",
            correlationScore=0.85,
            insights=[
                "Alto allineamento tra vendite e inventario",
                "Possibili discrepanze su alcuni SKU"
            ]
        )
    ]

    response = IntegrationCorrelationResponse(
        results=mock_results,
        totalPairs=len(mock_results),
        message=f"Correlazione completata per tipo '{request.correlationType}'."
    )
    return response


@router.get(
    "/inventoryImpact",
    response_model= IntegrationInventoryImpactResponse,
    status_code=status.HTTP_200_OK,
    **api_docs(integration_inventory_impact_desc, integration_inventory_impact_params, integration_inventory_optimization_response)
)
async def inventory_impact(
        timeframe: int = Query(..., description="Periodo di analisi in giorni")
):
    # Dati mockati
    mock_details = [
        IntegrationInventoryImpactEntry(category="bevande", stockValue=5000.0, cashFlowImpact=-1200.0),
        IntegrationInventoryImpactEntry(category="alimentari", stockValue=8000.0, cashFlowImpact=-2500.0),
        IntegrationInventoryImpactEntry(category="pulizia", stockValue=3000.0, cashFlowImpact=-700.0),
    ]

    total_stock_value = sum(item.stockValue for item in mock_details)
    total_cash_flow_impact = sum(item.cashFlowImpact for item in mock_details)

    response = IntegrationInventoryImpactResponse(
        timeframe=timeframe,
        totalStockValue=total_stock_value,
        totalCashFlowImpact=total_cash_flow_impact,
        details=mock_details,
        message=f"Analisi completata per un periodo di {timeframe} giorni."
    )

    return response