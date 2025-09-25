from datetime import date, timedelta
import random
from typing import List
from fastapi import APIRouter, Query
from starlette import status

from metadata.apiDocs import api_docs
from metadata.cashflowdocs import cashflow_crunch_detection_desc, cashflow_crunch_detection_params, \
    cashflow_crunch_detection_response, cashflow_accounting_data_desc, cashflow_accounting_data_params, \
    cashflow_accounting_data_response
from schemas.request.cashflowRequest import AccountingDataRequest
from schemas.response.cashflowResponse import CrunchDetectionResponse, CrunchDetectionLiquidityCrisis, \
    AccountingDataResponse

router = APIRouter(
    prefix="/cashflow",
    tags=["cashflow"]
)


@router.get(
    "/crunchDetection",
    response_model=CrunchDetectionResponse,
    status_code=status.HTTP_200_OK,
    **api_docs(cashflow_crunch_detection_desc, cashflow_crunch_detection_params, cashflow_crunch_detection_response)
)
async def get_crunch_detection(
    confidence_threshold: float = Query(..., ge=0.0, le=1.0, description="Soglia minima di confidenza", alias="confidenceThreshold"),
    forecast_horizon: int = Query(..., ge=1, le=365, description="Orizzonte temporale di previsione in giorni", alias="forecastHorizon")
):
    # dati mockati
    today = date.today()
    crises: List[CrunchDetectionLiquidityCrisis] = []

    cluster_starts = random.sample(range(forecast_horizon), k=max(1, forecast_horizon // 30))
    for i in range(forecast_horizon):
        prob = round(random.uniform(0.0, 0.4), 2)
        if any(abs(i - start) <= 2 for start in cluster_starts):
            prob = round(random.uniform(0.6, 1.0), 2)

        if prob >= confidence_threshold:
            crises.append(
                CrunchDetectionLiquidityCrisis(
                    liquidityCrisis=today + timedelta(days=i),
                    probability=prob
                )
            )
    return CrunchDetectionResponse(
        forecast_horizon=forecast_horizon,
        confidence_threshold=confidence_threshold,
        crises=crises
    )


@router.post(
    "/accountingDdata",
    response_model=AccountingDataResponse,
    status_code=status.HTTP_200_OK,
    **api_docs(cashflow_accounting_data_desc, cashflow_accounting_data_params, cashflow_accounting_data_response)
)
async def update_accounting_data(accountingDataRequest: AccountingDataRequest):
    updated_count = len(accountingDataRequest.data)
    total_amount = sum(item.amount for item in accountingDataRequest.data)

    response = AccountingDataResponse(
        updatedCount=updated_count,
        totalAmount=total_amount,
        message=f"Aggiornati {updated_count} record di tipo {accountingDataRequest.dataType}."
    )
    return response

