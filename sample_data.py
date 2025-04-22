from models import GolfClub

sample_clubs = [
    GolfClub(
        club_id="drv001",
        name="TaylorMade Stealth 2",
        brand="TaylorMade",
        type="driver",
        loft=9.0,
        shaft_flex="stiff",
        handicap_range_min=5,
        handicap_range_max=15,
        play_style="aggressive",
        description="A power-focused driver with a carbon face for low spin and high ball speed."
    ),
    GolfClub(
        club_id="irn001",
        name="Callaway Apex Pro 21",
        brand="Callaway",
        type="iron",
        loft=34.0,
        shaft_flex="regular",
        handicap_range_min=5,
        handicap_range_max=12,
        play_style="balanced",
        description="Forged feel with modern distance tech; great for low to mid handicaps."
    ),
    GolfClub(
        club_id="wge001",
        name="Titleist Vokey SM9",
        brand="Titleist",
        type="wedge",
        loft=56.0,
        shaft_flex="stiff",
        handicap_range_min=0,
        handicap_range_max=20,
        play_style="conservative",
        description="High spin and precision around the green."
    ),
    GolfClub(
        club_id="ptt001",
        name="Odyssey White Hot OG",
        brand="Odyssey",
        type="putter",
        shaft_flex=None,
        handicap_range_min=0,
        handicap_range_max=30,
        play_style="balanced",
        description="Classic insert feel with a timeless design."
    ),
    GolfClub(
        club_id="wd001",
        name="Ping G430 Max Fairway Wood",
        brand="Ping",
        type="wood",
        loft=15.0,
        shaft_flex="senior",
        handicap_range_min=10,
        handicap_range_max=25,
        play_style="conservative",
        description="Forgiving fairway wood designed for maximum launch."
    ),
]
