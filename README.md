# FPL-Insights

A Python project to fetch and analyze Fantasy Premier League (FPL) data, focusing on gameweek performance and the top 10 overall teams.

## Structure
- `scripts/fetch_fpl_data.py`: Downloads FPL API data and saves it as JSONs in `data/`.
- `notebooks/fpl_analysis.ipynb`: Jupyter Notebook for weekly analysis with visualizations.
- `data/`: Stores fetched JSONs.

## Setup
1. Clone the repo: `git clone https://github.com/yourusername/FPL-Insights.git`
2. Navigate to the project: `cd FPL-Insights`
3. Create a virtual environment: `python3 -m venv venv`
4. Activate it:
   - macOS/Linux: `source venv/bin/activate`
   - Windows: `venv\Scripts\activate`
5. Install dependencies: `pip install requests pandas matplotlib seaborn`
6. Run the script: `python scripts/fetch_fpl_data.py`
7. Open the notebook: `jupyter notebook notebooks/fpl_analysis.ipynb`
8. Deactivate when done: `deactivate`

## Usage
- Update the gameweek in `fetch_fpl_data.py` and run it weekly.
- Adjust the `GW` variable in the notebook to analyze different weeks.