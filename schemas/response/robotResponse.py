from pydantic import BaseModel
from typing import Literal, Optional, Dict, List


class RobotControlResponse(BaseModel):
    message: str
    status: str


class RobotImageResponse(BaseModel):
    image_id: str
    status: str


class RobotRecognizedProduct(BaseModel):
    name: str
    quantity: int
    confidence: float


class RobotRecognizedResponse(BaseModel):
    image_id: str
    recognized_products: List[RobotRecognizedProduct]


class RobotStatusResponse(BaseModel):
    robot_status: str
    position: str
    battery_level: float
    current_activity: str


class RobotScheduleScan(BaseModel):
    zone_id: int
    start_time: str
    priority: str


class RobotScheduleResponse(BaseModel):
    message: str
    scheduled_scans: List[RobotScheduleScan]
