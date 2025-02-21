# FPL-Insights

A Python project to fetch and analyze Fantasy Premier League (FPL) data, focusing on gameweek performance and the top 10 overall teams.

## Structure
- `scripts/fetch_fpl_data.py`: Downloads FPL API data and saves it as JSONs in `data/`.
- `notebooks/fpl_analysis.ipynb`: Jupyter Notebook for weekly analysis with visualizations.
- `data/`: Stores fetched JSONs (not tracked in Git).

## Setup
1. Clone the repo: `git clone https://github.com/yourusername/FPL-Insights.git`
2. Install dependencies: `pip install requests pandas matplotlib seaborn jupyter`
3. Run the script: `python scripts/fetch_fpl_data.py`
4. Open the notebook: `jupyter notebook notebooks/fpl_analysis.ipynb`

## Usage
- Update the gameweek in `fetch_fpl_data.py` and run it weekly.
- Adjust the `GW` variable in the notebook to analyze different weeks.