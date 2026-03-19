from scraper import run_scraper
from processor import transform_to_dataframe
from database import save_to_database, generate_summary
import sqlite3
import pandas as pd

if __name__ == "__main__":
    print("Starting NMRC ETL Pipeline...")

    # 1. Extract
    stations, timestamp = run_scraper()

    if stations:
        print(f"Successfully grabbed {len(stations)} stations. Transforming...")

        # 2. Transform
        final_df = transform_to_dataframe(stations, timestamp)

        # 3. Load & Summarize
        save_to_database(final_df)
        generate_summary(final_df)

        print("\nPipeline execution complete!\n")
        
        # --- NEW CODE ADDED HERE ---
        # 4. Display Final Output
        conn = sqlite3.connect('metro_data.db')
        query = """
        SELECT
            source AS Source,
            destination AS Destination,
            intermediate_stations AS "Intermediate Stations",
            fare_inr AS Fare,
            distance_km AS Distance,
            travel_time_mins AS Time
        FROM metro_fares
        """
        final_output_df = pd.read_sql_query(query, conn)
        conn.close()

        with pd.option_context('display.max_rows', None):
            print("--- FULL FINAL OUTPUT ---")
            print(final_output_df.to_string(index=False))

    else:
        print("Extraction failed. Pipeline aborted.")