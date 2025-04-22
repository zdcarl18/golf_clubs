from sample_data import sample_clubs

for club in sample_clubs:
    print(f"{club.name} ({club.type}) - Best for handicaps {club.handicap_range_min}–{club.handicap_range_max}")