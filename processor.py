import pandas as pd

def calculate_fare(stations_travelled):
    if stations_travelled == 1: return 10
    elif stations_travelled == 2: return 15
    elif 3 <= stations_travelled <= 6: return 20
    elif 7 <= stations_travelled <= 9: return 30
    elif 10 <= stations_travelled <= 14: return 40
    elif stations_travelled >= 15: return 50
    return 0

def transform_to_dataframe(stations, scraped_at):
    routes_data = []
    for src_idx, source in enumerate(stations):
        for dst_idx, destination in enumerate(stations):
            if source == destination:
                continue
                
            stations_travelled = abs(src_idx - dst_idx)
            intermediate_stations = stations_travelled - 1
            distance_km = round(stations_travelled * 1.4, 2)
            time_mins = stations_travelled * 3
            fare = calculate_fare(stations_travelled)
            
            routes_data.append({
                "source": source,
                "destination": destination,
                "intermediate_stations": intermediate_stations,
                "fare_inr": fare,
                "distance_km": distance_km,
                "travel_time_mins": time_mins,
                "scraped_at": scraped_at
            })
            
    df = pd.DataFrame(routes_data)
    df['fare_inr'] = df['fare_inr'].astype(int)
    df['distance_km'] = df['distance_km'].astype(float)
    return df