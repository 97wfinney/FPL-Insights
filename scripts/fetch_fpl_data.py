import requests
import json
import os
from datetime import datetime

# Base directory for saving JSONs
BASE_DIR = "data"
os.makedirs(BASE_DIR, exist_ok=True)

# API Endpoints
BOOTSTRAP_URL = "https://fantasy.premierleague.com/api/bootstrap-static/"
FIXTURES_URL = "https://fantasy.premierleague.com/api/fixtures/"
OVERALL_LEAGUE_URL = "https://fantasy.premierleague.com/api/leagues-classic/1/standings/"
PICKS_URL_TEMPLATE = "https://fantasy.premierleague.com/api/entry/{manager_id}/event/{gw}/picks/"

# Function to save JSON
def save_json(data, filepath):
    with open(filepath, "w") as f:
        json.dump(data, f)
    print(f"Saved: {filepath}")

# Fetch and save data for a specific gameweek
def fetch_fpl_data(gameweek):
    # Create gameweek-specific subfolder
    gw_dir = os.path.join(BASE_DIR, f"gw{gameweek}")
    os.makedirs(gw_dir, exist_ok=True)

    # Bootstrap-static
    bootstrap = requests.get(BOOTSTRAP_URL).json()
    save_json(bootstrap, os.path.join(gw_dir, f"bootstrap_gw{gameweek}.json"))

    # Fixtures
    fixtures = requests.get(FIXTURES_URL).json()
    save_json(fixtures, os.path.join(gw_dir, f"fixtures_gw{gameweek}.json"))

    # Overall league standings (top 50)
    standings = requests.get(OVERALL_LEAGUE_URL).json()
    save_json(standings, os.path.join(gw_dir, f"overall_standings_gw{gameweek}.json"))

    # Get top 10 manager IDs
    top_10 = standings["standings"]["results"][:10]
    manager_ids = [entry["entry"] for entry in top_10]

    # Fetch and save picks for top 10 managers
    picks_dir = os.path.join(gw_dir, "picks")
    os.makedirs(picks_dir, exist_ok=True)
    for manager_id in manager_ids:
        picks_url = PICKS_URL_TEMPLATE.format(manager_id=manager_id, gw=gameweek)
        picks = requests.get(picks_url).json()
        save_json(picks, os.path.join(picks_dir, f"picks_{manager_id}_gw{gameweek}.json"))

if __name__ == "__main__":
    # Example: Fetch data for GW 1 (replace with current GW as needed)
    current_gw = 1  # You could dynamically determine this from bootstrap["events"]
    fetch_fpl_data(current_gw)
    print(f"Data fetched and saved for GW {current_gw} on {datetime.now().strftime('%Y-%m-%d')}")