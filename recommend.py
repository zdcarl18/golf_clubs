from models import GolfClub, GolferProfile
from typing import Optional, Literal

def recommend_clubs(profile, clubs, club_type=None, max_price=None, gender=None):
    matches = []

    for club in clubs:
        # Basic matching
        if club_type and club.type != club_type:
            continue
        if max_price and club.price and club.price > max_price:
            continue
        if gender and club.player_gender and club.player_gender.lower() != gender.lower():
            continue

        # Scoring (can be more complex later)
        score = 0
        if club.handicap_range_min and club.handicap_range_max:
            if club.handicap_range_min <= profile.handicap <= club.handicap_range_max:
                score += 2

        if club.play_style and club.play_style.lower() == profile.preferred_play_style.lower():
            score += 1

        if club.target_audience and club.target_audience.lower() in profile.experience_level.lower():
            score += 1

        matches.append((club, score))

    matches.sort(key=lambda x: x[1], reverse=True)
    return [club for club, score in matches if score > 0]




