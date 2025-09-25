from typing import Optional
from fastapi import APIRouter, Query
from starlette import status

from metadata.apiDocs import api_docs
from metadata.posDocs import pos_connect_params, pos_connect_desc, pos_connect_response
from schemas.request.posRequest import PosConnectRequest
from schemas.response.posResponse import PosConnectResponse

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

