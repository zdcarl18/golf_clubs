import csv
from typing import List, Optional
from models import GolfClub

def load_clubs_from_csv(filepath: str) -> List[GolfClub]:
    clubs = []
    with open(filepath, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            club = GolfClub(
                club_id=row['club_id'],
                name=row['name'],
                brand=row['brand'],
                type=row['type'],
                loft=float(row['loft']) if row['loft'] else None,
                shaft_flex=row['shaft_flex'] if row['shaft_flex'] != 'None' else None,
                handicap_range_min=int(row['handicap_range_min']) if row['handicap_range_min'] else None,
                handicap_range_max=int(row['handicap_range_max']) if row['handicap_range_max'] else None,
                play_style=row['play_style'] if row['play_style'] else None,
                description=row['description']
            )
            clubs.append(club)
    return clubs

# Example usage

if __name__ == "__main__":
    clubs = load_clubs_from_csv("data/clubs.csv")
    for club in clubs:
        print(f"{club.name} ({club.type}) - {club.play_style} - Handicap: {club.handicap_range_min}-{club.handicap_range_max}")

