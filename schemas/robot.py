from pydantic import BaseModel
from typing import Literal, Optional, Dict, List


class RobotControlRequest(BaseModel):
    command: Literal["start_scan", "stop_scan", "return_to_base"]
    zone_id: int
    priority: Literal["alta", "media", "bassa"]


class RobotControlResponse(BaseModel):
    message: str
    status: str


class RobotImageRequest(BaseModel):
    image_data: str
    timestamp: str
    location: str
    metadata: Optional[Dict] = None


class RobotImageResponse(BaseModel):
    image_id: str
    status: str


class RobotRecognitionRequest(BaseModel):
    image_id: str
    recognition_mode: Literal["rapida", "accurata"]


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


class RobotScheduleScanItem(BaseModel):
    zone_id: int
    start_time: str


class RobotScheduleRequest(BaseModel):
    schedule: List[RobotScheduleScanItem]
    priority_zones: List[int]


class RobotScheduleScan(BaseModel):
    zone_id: int
    start_time: str
    priority: str


class RobotScheduleResponse(BaseModel):
    message: str
    scheduled_scans: List[RobotScheduleScan]
