import csv
from models import GolfClub

def load_clubs_from_csv(path: str) -> list[GolfClub]:
    clubs = []
    with open(path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                club = GolfClub(
                    club_id=row["club_id"],
                    name=row["name"],
                    brand=row["brand"],
                    type=row["type"],
                    loft=float(row["loft"]) if row["loft"] else None,
                    shaft_flex=row["shaft_flex"] or None,
                    shaft_material=row["shaft_material"] or None,
                    head_material=row["head_material"] or None,
                    length=float(row["length"]) if row["length"] else None,
                    lie_angle=float(row["lie_angle"]) if row["lie_angle"] else None,
                    swing_weight=row["swing_weight"] or None,
                    launch_angle=float(row["launch_angle"]) if row["launch_angle"] else None,
                    spin_rate=int(row["spin_rate"]) if row["spin_rate"] else None,
                    forgiveness_rating=int(row["forgiveness_rating"]) if row["forgiveness_rating"] else None,
                    distance_rating=int(row["distance_rating"]) if row["distance_rating"] else None,
                    workability_rating=int(row["workability_rating"]) if row["workability_rating"] else None,
                    adjustable=row["adjustable"].lower() == "true" if row["adjustable"] else None,
                    price=float(row["price"]) if row["price"] else None,
                    year_released=int(row["year_released"]) if row["year_released"] else None,
                    player_gender=row["player_gender"] or None,
                    target_audience=row["target_audience"] or None,
                    play_style=row["play_style"] or None,
                    handicap_range_min=int(row["handicap_range_min"]) if row["handicap_range_min"] else None,
                    handicap_range_max=int(row["handicap_range_max"]) if row["handicap_range_max"] else None,
                    description=row["description"] or None,
                    image_url=row["image_url"] or None,
                )
                clubs.append(club)
            except Exception as e:
                print(f"⚠️ Skipping row due to error: {e}")
    return clubs

# Example usage

if __name__ == "__main__":
    clubs = load_clubs_from_csv("data/clubs.csv")
    for club in clubs:
        print(f"{club.name} ({club.type}) - {club.play_style} - Handicap: {club.handicap_range_min}-{club.handicap_range_max}")

