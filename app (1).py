import pandas as pd
from pybaseball import statcast
from datetime import datetime

# Define the season year
season_year = 2024  # Update to the desired season
start_date = f"{season_year}-03-01"
end_date = f"{season_year}-10-31"

# Fetch Statcast data for the specified date range
print(f"Fetching Statcast data from {start_date} to {end_date}...")
data = statcast(start_dt=start_date, end_dt=end_date)

# Filter out entries without pitcher name or pitch type
data = data[['player_name', 'pitch_type']].dropna()

# Map pitch type codes to full names
pitch_type_mapping = {
    'FF': 'Four-Seam Fastball',
    'FT': 'Two-Seam Fastball',
    'SI': 'Sinker',
    'FC': 'Cutter',
    'FS': 'Splitter',
    'SL': 'Slider',
    'CH': 'Changeup',
    'CU': 'Curveball',
    'KC': 'Knuckle Curve',
    'KN': 'Knuckleball',
    'EP': 'Eephus',
    'SC': 'Screwball',
    'ST': 'Sweeper',
    'SV': 'Slurve',
    'UN': 'Unknown'
}

# Map pitch type codes to full names
data['pitch_type_full'] = data['pitch_type'].map(pitch_type_mapping)

# Group by pitcher and aggregate unique pitch types
pitcher_pitch_types = data.groupby('player_name')['pitch_type_full'].unique().reset_index()

# Sort by pitcher name
pitcher_pitch_types = pitcher_pitch_types.sort_values('player_name')

# Save to CSV
output_filename = f"mlb_pitchers_pitch_types_{season_year}.csv"
pitcher_pitch_types.to_csv(output_filename, index=False)

print(f"Pitch types per pitcher saved to {output_filename}")
