import argparse
from models import GolferProfile
from recommend import recommend_clubs
from sample_data import sample_clubs

def main():
    parser = argparse.ArgumentParser(description="Golf Club Recommendation Tool")

    parser.add_argument("--handicap", type=float, required=True, help="Your golf handicap")
    parser.add_argument("--play-style", type=str, choices=["aggressive", "balanced", "conservative"], required=True, help="Your play style")
    parser.add_argument("--experience", type=str, choices=["beginner", "intermediate", "advanced"], default="intermediate", help="Your experience level")
    parser.add_argument("--club-type", type=str, choices=["driver", "wood", "iron", "wedge", "putter"], help="Filter by club type (optional)")
    parser.add_argument("--max", type=int, default=3, help="Number of recommendations to return")

    args = parser.parse_args()

    profile = GolferProfile(
        golfer_id="cli_user",
        name="CLI User",
        handicap=args.handicap,
        preferred_play_style=args.play_style,
        experience_level=args.experience,
    )

    results = recommend_clubs(profile, sample_clubs, club_type=args.club_type, max_results=args.max)

    print("\n🏌️ Recommended Clubs:")
    for club in results:
        print(f"✅ {club.name} ({club.type}) — For {club.play_style} players, handicap {club.handicap_range_min}-{club.handicap_range_max}")

if __name__ == "__main__":
    main()
