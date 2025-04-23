import streamlit as st
import pandas as pd
from load_from_csv import load_clubs_from_csv

# Load club data
clubs = load_clubs_from_csv("data/clubs.csv")
df = pd.DataFrame([club.__dict__ for club in clubs])

# Sidebar input
st.sidebar.header("🧑 Golfer Profile")
handicap = st.sidebar.slider("Handicap", min_value=0, max_value=36, value=12)
play_style = st.sidebar.selectbox("Play Style", ["aggressive", "balanced", "conservative"])
experience = st.sidebar.selectbox("Experience Level", ["beginner", "intermediate", "advanced"])
club_type = st.sidebar.selectbox("Club Type (optional)", [""] + sorted(df["type"].dropna().unique().tolist()))

# Additional filters
max_price = st.sidebar.slider("Max Price", min_value=100, max_value=1000, value=1000, step=50)
gender_filter = st.sidebar.selectbox("Player Gender (optional)", [""] + sorted(df["player_gender"].dropna().unique().tolist()))
shaft_material = st.sidebar.selectbox("Shaft Material (optional)", [""] + sorted(df["shaft_material"].dropna().unique().tolist()))
shaft_flex = st.sidebar.selectbox("Shaft Flex (optional)", [""] + sorted(df["shaft_flex"].dropna().unique().tolist()))
head_material = st.sidebar.selectbox("Head Material (optional)", [""] + sorted(df["head_material"].dropna().unique().tolist()))
lie_angle = st.sidebar.selectbox("Lie Angle (optional)", [""] + sorted(df["lie_angle"].dropna().unique().tolist()))
launch_angle = st.sidebar.selectbox("Launch Angle (optional)", [""] + sorted(df["launch_angle"].dropna().unique().tolist()))
min_forgiveness = st.sidebar.slider("Min Forgiveness Rating", min_value=0, max_value=10, value=0)
min_distance = st.sidebar.slider("Min Distance Rating", min_value=0, max_value=10, value=0)
min_workability = st.sidebar.slider("Min Workability Rating", min_value=0, max_value=10, value=0)

# Filter the DataFrame
filtered_df = df[
    (df["price"] <= max_price) &
    (df["forgiveness_rating"] >= min_forgiveness) &
    (df["distance_rating"] >= min_distance) &
    (df["workability_rating"] >= min_workability)
]

if club_type:
    filtered_df = filtered_df[filtered_df["type"] == club_type]
if gender_filter:
    filtered_df = filtered_df[filtered_df["player_gender"] == gender_filter]
if shaft_material:
    filtered_df = filtered_df[filtered_df["shaft_material"] == shaft_material]
if shaft_flex:
    filtered_df = filtered_df[filtered_df["shaft_flex"] == shaft_flex]
if head_material:
    filtered_df = filtered_df[filtered_df["head_material"] == head_material]
if lie_angle:
    filtered_df = filtered_df[filtered_df["lie_angle"] == lie_angle]
if launch_angle:
    filtered_df = filtered_df[filtered_df["launch_angle"] == launch_angle]

# Display results
st.header("🏌️ Filtered Golf Clubs")
if not filtered_df.empty:
    for _, row in filtered_df.iterrows():
        st.image(row["image_url"], width=300)
        st.markdown(f"### {row['name']} ({row['type'].title()})")
        st.markdown(f"**Brand**: {row['brand']}  \n"
                    f"**Flex**: {row['shaft_flex']}, **Shaft**: {row['shaft_material']}  \n"
                    f"**Head**: {row['head_material']}, **Lie Angle**: {row['lie_angle']}, **Launch**: {row['launch_angle']}  \n"
                    f"**Forgiveness**: {row['forgiveness_rating']}/10, **Distance**: {row['distance_rating']}/10, "
                    f"**Workability**: {row['workability_rating']}/10  \n"
                    f"**Price**: ${row['price']:.2f}, **Year**: {row['year_released']}  \n"
                    f"**Gender**: {row['player_gender']}, **Adjustable**: {'Yes' if row['adjustable'] else 'No'}")
        st.markdown(f"*{row['description']}*")
        st.divider()
else:
    st.warning("No clubs found with the selected filters.")
