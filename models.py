from pydantic import BaseModel
from typing import Optional, Literal

class GolfClub(BaseModel):
    club_id: str
    name: str
    brand: str
    type: str
    loft: Optional[float]
    shaft_flex: Optional[str]
    shaft_material: Optional[str]
    head_material: Optional[str]
    length: Optional[float]
    lie_angle: Optional[float]
    swing_weight: Optional[str]
    launch_angle: Optional[float]
    spin_rate: Optional[int]
    forgiveness_rating: Optional[int]
    distance_rating: Optional[int]
    workability_rating: Optional[int]
    adjustable: Optional[bool]
    price: Optional[float]
    year_released: Optional[int]
    player_gender: Optional[str]
    target_audience: Optional[str]
    play_style: Optional[str]
    handicap_range_min: Optional[int]
    handicap_range_max: Optional[int]
    description: Optional[str]
    image_url: Optional[str]


class GolferProfile(BaseModel):
    golfer_id: str
    name: Optional[str]
    handicap: float
    preferred_play_style: Literal['aggressive', 'balanced', 'conservative']
    experience_level: Literal['beginner', 'intermediate', 'advanced']