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

# Function to get current gameweek
def get_current_gameweek():
    bootstrap = requests.get(BOOTSTRAP_URL).json()
    for event in bootstrap["events"]:
        if event.get("is_current", False):
            return event["id"]
    # Fallback: If no current GW, return the latest finished GW or 1
    return max(event["id"] for event in bootstrap["events"] if event["finished"]) or 1

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

    # Get top 10 manager IDs and their picks in a single JSON
    top_10 = standings["standings"]["results"][:10]
    top10_picks = {}
    for entry in top_10:
        manager_id = entry["entry"]
        picks_url = PICKS_URL_TEMPLATE.format(manager_id=manager_id, gw=gameweek)
        picks = requests.get(picks_url).json()
        top10_picks[manager_id] = {
            "manager_name": entry["player_name"],
            "team_name": entry["entry_name"],
            "picks": picks["picks"],
            "active_chip": picks.get("active_chip", None)
        }

    # Save top 10 picks as a single JSON file
    top10_picks_path = os.path.join(gw_dir, f"top10_picks_gw{gameweek}.json")
    save_json(top10_picks, top10_picks_path)

if __name__ == "__main__":
    current_gw = get_current_gameweek()
    fetch_fpl_data(current_gw)
    print(f"Data fetched and saved for GW {current_gw} on {datetime.now().strftime('%Y-%m-%d')}")