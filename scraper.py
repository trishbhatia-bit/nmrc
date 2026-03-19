import requests
from bs4 import BeautifulSoup
from datetime import datetime

def extract_station_list(soup):
    stations = []
    tables = soup.find_all('table')
    if tables:
        station_table = tables[0]
        rows = station_table.find_all('tr')
        for row in rows[1:]:
            columns = row.find_all('td')
            if len(columns) > 0:
                station_name = columns[0].text.strip()
                if station_name and station_name.lower() != "station name":
                    stations.append(station_name)
    return stations

def run_scraper():
    url = "https://www.nmrcnoida.com/Passenger-Information/Metro-Rail/Train-Timings"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    stations = extract_station_list(soup)
    scraped_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return stations, scraped_at