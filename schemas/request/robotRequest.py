from pydantic import BaseModel
from typing import Literal, Optional, Dict, List


class RobotControlRequest(BaseModel):
    command: Literal["start_scan", "stop_scan", "return_to_base"]
    zone_id: int
    priority: Literal["alta", "media", "bassa"]


class RobotImageRequest(BaseModel):
    image_data: str
    timestamp: str
    location: str
    metadata: Optional[Dict] = None


class RobotRecognitionRequest(BaseModel):
    image_id: str
    recognition_mode: Literal["rapida", "accurata"]


class RobotScheduleScanItem(BaseModel):
    zone_id: int
    start_time: str


class RobotScheduleRequest(BaseModel):
    schedule: List[RobotScheduleScanItem]
    priority_zones: List[int]




