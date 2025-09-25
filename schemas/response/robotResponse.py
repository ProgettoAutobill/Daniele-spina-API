from pydantic import BaseModel
from typing import List


class RobotControlResponse(BaseModel):
    message: str
    status: str


class RobotImageResponse(BaseModel):
    imageId: str
    status: str


class RobotRecognizedProduct(BaseModel):
    name: str
    quantity: int
    confidence: float


class RobotRecognizedResponse(BaseModel):
    imageId: str
    recognizedProducts: List[RobotRecognizedProduct]


class RobotStatusResponse(BaseModel):
    robotStatus: str
    position: str
    batteryLevel: float
    currentActivity: str


class RobotScheduleScan(BaseModel):
    zoneId: int
    startTime: str
    priority: str


class RobotScheduleResponse(BaseModel):
    message: str
    scheduledScans: List[RobotScheduleScan]
