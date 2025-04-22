from pydantic import BaseModel, Field
from typing import Literal, Optional

class GolfClub(BaseModel):
    club_id: str
    name: str
    brand: str
    type: Literal['driver', 'wood', 'iron', 'wedge', 'putter']
    loft: Optional[float] = Field(None, description="Loft angle in degrees")
    shaft_flex: Optional[Literal['extra stiff', 'stiff', 'regular', 'senior', 'ladies']]
    handicap_range_min: Optional[int]
    handicap_range_max: Optional[int]
    play_style: Optional[Literal['aggressive', 'balanced', 'conservative']]
    description: Optional[str]

class GolferProfile(BaseModel):
    golfer_id: str
    name: Optional[str]
    handicap: float
    preferred_play_style: Literal['aggressive', 'balanced', 'conservative']
    experience_level: Literal['beginner', 'intermediate', 'advanced']