from fastapi import APIRouter
from starlette import status

from metadata.apiDocs import api_docs
from metadata.erpDocs import erp_connect_desc, erp_connect_params, erp_connect_response
from schemas.request.erpRequest import ErpConnectRequest
from schemas.response.erpResponse import ErpConnectResponse

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
