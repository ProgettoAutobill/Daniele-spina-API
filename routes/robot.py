from fastapi import APIRouter, Query
from starlette import status
from metadata.apiDocs import api_docs
from metadata.robotDocs import robot_control_params, robot_control_response, robot_control_desc, robot_images_desc, \
    robot_images_params, robot_images_response, robot_recognition_desc, robot_status_desc, robot_schedule_desc, \
    robot_recognition_response, robot_status_response, robot_schedule_response, robot_recognition_params, \
    robot_status_params, robot_schedule_params
from schemas.request.robotRequest import RobotControlRequest, RobotImageRequest, RobotRecognitionRequest, \
    RobotScheduleRequest
from schemas.response.robotResponse import RobotControlResponse, RobotImageResponse, RobotRecognizedResponse, \
    RobotRecognizedProduct, RobotStatusResponse, RobotScheduleResponse, RobotScheduleScan

router = APIRouter(
    prefix="/api/robot",
    tags=["robot"]
)


@router.post(
    "/control",
    response_model=RobotControlResponse,
    status_code=status.HTTP_200_OK,
    **api_docs(robot_control_desc, robot_control_params, robot_control_response)
)
async def control(command: RobotControlRequest):
    return {"message": f"Comando ricevuto: {command.command}", "status": "in esecuzione"}


@router.post(
    "/images",
    response_model=RobotImageResponse,
    status_code=status.HTTP_200_OK,
    **api_docs(robot_images_desc, robot_images_params, robot_images_response)
)
async def images(image: RobotImageRequest):
    return {"imageId": "1", "status": "ok"}


@router.post(
    "/recognition",
    response_model=RobotRecognizedResponse,
    status_code=status.HTTP_200_OK,
    **api_docs(robot_recognition_desc, robot_recognition_params, robot_recognition_response)
)
async def recognition(recognition: RobotRecognitionRequest):
    mock_products = [
        RobotRecognizedProduct(name="Latte", quantity=2, confidence=0.95),
        RobotRecognizedProduct(name="Pane", quantity=1, confidence=0.87),
        RobotRecognizedProduct(name="Uova", quantity=12, confidence=0.92)
    ]

    return RobotRecognizedResponse(
        imageId=recognition.imageId,
        recognizedProducts=mock_products
    )


@router.get(
    "/status",
    response_model=RobotStatusResponse,
    status_code=status.HTTP_200_OK,
    **api_docs(robot_status_desc, robot_status_params, robot_status_response)
)
async def get_status(details_level: str = Query(..., alias="detailsLevel")):
    return {"robotStatus": "status 1", "position": "3", "batteryLevel": 0.75, "currentActivity": "current"}


@router.put(
    "/schedule",
    response_model=RobotScheduleResponse,
    status_code=status.HTTP_200_OK,
    **api_docs(robot_schedule_desc, robot_schedule_params, robot_schedule_response)
)
async def schedule(schedule: RobotScheduleRequest):
    mock_schedule_list = [
        RobotScheduleScan(zoneId=1, startTime="2025-09-23T10:00:00Z", priority="alta"),
        RobotScheduleScan(zoneId=2, startTime="2025-09-23T14:00:00Z", priority="media"),
        RobotScheduleScan(zoneId=3, startTime="2025-09-24T09:00:00Z", priority="bassa")
    ]

    return RobotScheduleResponse(
        message="schedulazione avvenuta con successo",
        scheduledScans=mock_schedule_list
    )
