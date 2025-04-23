import streamlit as st
from load_from_csv import load_clubs_from_csv
from models import GolferProfile
from recommend import recommend_clubs

# Load club data
clubs = load_clubs_from_csv("data/clubs.csv")

# Sidebar input
st.sidebar.header("🧑 Golfer Profile")
handicap = st.sidebar.slider("Handicap", min_value=0, max_value=36, value=12)
play_style = st.sidebar.selectbox("Play Style", ["aggressive", "balanced", "conservative"])
experience = st.sidebar.selectbox("Experience Level", ["beginner", "intermediate", "advanced"])
club_type = st.sidebar.selectbox("Club Type (optional)", ["", "driver", "wood", "iron", "wedge", "putter"])

# Additional filters
max_price = st.sidebar.slider("Max Price", min_value=100, max_value=1000, value=1000, step=50)
gender_filter = st.sidebar.selectbox("Player Gender (optional)", ["", "men", "women", "unisex"])


# Submit button
if st.sidebar.button("Get Recommendations"):

    profile = GolferProfile(
        golfer_id="web_user",
        name="Web User",
        handicap=handicap,
        preferred_play_style=play_style,
        experience_level=experience
    )

    # Run recommender
    results = recommend_clubs(
        profile,
        clubs,
        club_type=club_type if club_type else None,
        max_price=max_price,
     gender=gender_filter if gender_filter else None
    )

    # Display results
    st.header("🏌️ Recommended Clubs")
    if results:
        for club in results:
            st.image(club.image_url, width=300)
            st.markdown(f"### {club.name} ({club.type.title()})")
            st.markdown(f"**Brand**: {club.brand}  \n"
                f"**Flex**: {club.shaft_flex}, **Shaft**: {club.shaft_material}  \n"
                f"**Forgiveness**: {club.forgiveness_rating}/10, **Distance**: {club.distance_rating}/10  \n"
                f"**Price**: ${club.price:.2f}, **Year**: {club.year_released}  \n"
                f"**Gender**: {club.player_gender}, **Adjustable**: {'Yes' if club.adjustable else 'No'}")
            st.markdown(f"*{club.description}*")
            st.divider()
    else:
        st.warning("No matching clubs found. Try adjusting your profile.")

else:
    st.info("Fill in your golfer profile and click 'Get Recommendations' to start.")
