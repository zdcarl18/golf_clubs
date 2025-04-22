from models import GolfClub, GolferProfile
from sample_data import sample_clubs
from typing import Optional

def recommend_clubs(
    profile: GolferProfile,
    clubs: list[GolfClub],
    club_type: Optional[str] = None,
    max_results: int = 3
) -> list[GolfClub]:
    matches = []

    for club in clubs:
        if club_type and club.type != club_type:
            continue

        score = 0

        if club.handicap_range_min is not None and club.handicap_range_max is not None:
            if club.handicap_range_min <= profile.handicap <= club.handicap_range_max:
                score += 1

        if club.play_style == profile.preferred_play_style:
            score += 1

        if score > 0:
            matches.append((score, club))

    sorted_matches = sorted(matches, key=lambda x: x[0], reverse=True)
    return [club for score, club in sorted_matches[:max_results]]


# Example usage

from models import GolferProfile
from recommend import recommend_clubs
from sample_data import sample_clubs

my_profile = GolferProfile(
    golfer_id="g001",
    name="Jamie",
    handicap=12.0,
    preferred_play_style="balanced",
    experience_level="intermediate"
)

recommendations = recommend_clubs(my_profile, sample_clubs)

for club in recommendations:
    print(f"✅ {club.name} ({club.type}) — Best for {club.play_style} players, handicap {club.handicap_range_min}-{club.handicap_range_max}")

