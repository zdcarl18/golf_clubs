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
        club_type=club_type if club_type else None
    )

    # Display results
    st.header("🏌️ Recommended Clubs")
    if results:
        for club in results:
            st.markdown(f"**{club.name}** ({club.type}) — _{club.play_style}_  \n"
                        f"Handicap: {club.handicap_range_min}-{club.handicap_range_max}  \n"
                        f"Brand: {club.brand}  \n"
                        f"{club.description}")
            st.divider()
    else:
        st.warning("No matching clubs found. Try adjusting your profile.")

else:
    st.info("Fill in your golfer profile and click 'Get Recommendations' to start.")
