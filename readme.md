# 🚇 Noida Metro (Aqua Line) ETL & Fare Explorer

A modular Python-based ETL (Extract, Transform, Load) pipeline that scrapes real-time station data from the Noida Metro Rail Corporation (NMRC) website, processes 420+ route combinations, and serves the data through a SQL database and a Streamlit web interface.

---

## 📌 Core Objectives
* **Data Crawling:** Extract sequential station lists from NMRC using `Requests` and `BeautifulSoup` (Bypassing encrypted JS payloads).
* **Data Transformation:** Programmatically generate all possible Source-Destination pairs using `Pandas`.
* **Calculation Engine:** Logic-based calculation for:
    * Fares (mapped to NMRC fare slabs)
    * Distance (estimated KM)
    * Travel Time (estimated minutes)
    * Intermediate Station Counts
* **Persistence:** Storage of cleaned data into a `SQLite3` database.
* **Frontend:** Interactive web dashboard built with `Streamlit`.

---

## 🛠️ Tech Stack
| Component | Tool |
| :--- | :--- |
| **Language** | Python 3.12+ |
| **Extraction** | BeautifulSoup4, Requests |
| **Processing** | Pandas |
| **Database** | SQLite3 |
| **Frontend** | Streamlit |
| **Environment** | Linux (Debian/Penguin) |

---

## 📂 Project Structure
```text
metro_project/
├── .venv/              # Virtual environment
├── main.py             # Master execution script (Pipeline Entry)
├── scraper.py          # Extraction module (Web Scraping)
├── processor.py        # Transformation module (Business Logic)
├── database.py         # Loading module (SQL & Logging)
├── app.py              # Streamlit Web Frontend
├── metro_data.db       # Generated SQLite Database
└── scraper.log         # Execution logs & error handling
