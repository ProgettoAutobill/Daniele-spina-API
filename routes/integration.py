from fastapi import APIRouter, Query, status
from starlette import status
from metadata.apiDocs import api_docs
from metadata.integrationDocs import integration_correlate_desc, integration_correlate_params, \
    integration_correlate_response
from schemas.request.integrationRequest import IntegrationCorrelationRequest
from schemas.response.integrationResponse import IntegrationCorrelationResponse, IntegrationCorrelationResult

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
