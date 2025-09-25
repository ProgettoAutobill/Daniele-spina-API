from typing import List

from fastapi import APIRouter, Query
from starlette import status
from metadata.apiDocs import api_docs
from metadata.dashboardDocs import dashboard_unified_desc, dashboard_unified_params, dashboard_unified_response
from schemas.response.dashboardResponse import DashboardUnifiedResponse

router = APIRouter(
    prefix="/dashboard",
    tags=["dashboard"]
)


@router.get(
    "/unified",
    response_model=DashboardUnifiedResponse,
    status_code=status.HTTP_200_OK,
    **api_docs(dashboard_unified_desc, dashboard_unified_params, dashboard_unified_response)
)
async def unified_dashboard(
    data_sources: List[str] = Query(..., description="Array di fonti dati da includere (es. robot, pos, erp)"),
    timeframe: str = Query(..., description="Periodo di analisi (es. giornaliero, settimanale, mensile)"),
    view_type: str = Query(..., description="Tipo di visualizzazione (operativa, strategica, finanziaria)")
):
    # Mock dei dati aggregati
    mock_data = {
        "robot": {"recognizedProducts": 125, "avgConfidence": 0.92},
        "pos": {"totalTransactions": 430, "salesValue": 15200.50, "returns": 25},
        "erp": {"invoices": 78, "orders": 54, "cashFlow": -3200.0}
    }

    # Filtra solo le fonti richieste
    filtered_data = {src: mock_data.get(src, {}) for src in data_sources}

    response = DashboardUnifiedResponse(
        dataSources=data_sources,
        timeframe=timeframe,
        viewType=view_type,
        aggregatedData=filtered_data,
        message=f"Dati aggregati per periodo '{timeframe}' e vista '{view_type}'."
    )
    return response