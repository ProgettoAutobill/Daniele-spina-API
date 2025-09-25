from pydantic import BaseModel
from typing import Literal, Optional, Dict, List


class RobotControlRequest(BaseModel):
    command: Literal["start_scan", "stop_scan", "return_to_base"]
    zoneId: int
    priority: Literal["alta", "media", "bassa"]


class RobotImageRequest(BaseModel):
    imageData: str
    timestamp: str
    location: str
    metadata: Optional[Dict] = None


class RobotRecognitionRequest(BaseModel):
    imageId: str
    recognitionMode: Literal["rapida", "accurata"]


class RobotScheduleScanItem(BaseModel):
    zoneId: int
    starTime: str


class RobotScheduleRequest(BaseModel):
    schedule: List[RobotScheduleScanItem]
    priorityZones: List[int]




