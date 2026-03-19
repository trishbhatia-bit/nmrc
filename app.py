import streamlit as st
import sqlite3
import pandas as pd

# 1. Set the page title and layout
st.set_page_config(page_title="NMRC Fare Explorer", layout="wide")
st.title("🚇 NMRC Aqua Line Fare Explorer")
st.markdown("An interactive dashboard to explore Metro routes, fares, and travel times.")

# 2. Fetch the data directly from your newly created database
@st.cache_data # This makes the app super fast by remembering the data
def load_data():
    conn = sqlite3.connect('metro_data.db')
    query = """
    SELECT 
        source AS Source, 
        destination AS Destination, 
        intermediate_stations AS "Intermediate Stations",
        fare_inr AS "Fare (₹)", 
        distance_km AS "Distance (km)", 
        travel_time_mins AS "Time (mins)"
    FROM metro_fares
    """
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

df = load_data()

# 3. Display the data as an interactive web table
st.dataframe(df, use_container_width=True, hide_index=True)

# 4. Add a quick summary at the bottom
st.success(f"Successfully loaded {len(df)} route combinations from the database.")