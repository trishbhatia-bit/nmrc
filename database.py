import sqlite3
import logging

logging.basicConfig(
    filename='scraper.log',
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def save_to_database(df, db_name="metro_data.db"):
    logging.info("Attempting to save data to SQLite database...")
    try:
        conn = sqlite3.connect(db_name)
        df.to_sql('metro_fares', conn, if_exists='replace', index=False)
        logging.info(f"Successfully saved {len(df)} records.")
        print(f"Data successfully saved to {db_name}")
    except Exception as e:
        logging.error(f"Database insertion failed: {e}")
        print("Database error occurred. Check scraper.log.")
    finally:
        if 'conn' in locals():
            conn.close()

def generate_summary(df):
    total_routes = len(df)
    max_fare = df['fare_inr'].max()
    max_distance = df['distance_km'].max()
    longest_trip = df['travel_time_mins'].max()
    
    print("\n--- PROJECT EXECUTION SUMMARY ---")
    print(f"Total Routes Extracted : {total_routes}")
    print(f"Maximum Fare           : ₹{max_fare}")
    print(f"Longest Route Distance : {max_distance} km")
    print(f"Maximum Travel Time    : {longest_trip} mins")
    print("---------------------------------")