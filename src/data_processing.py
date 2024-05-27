import pandas as pd

def load_data(file_path):
    try:
        data = pd.read_json(file_path)
        print("Data loaded successfully.")
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return pd.DataFrame()

def clean_data(data):
    # Extract relevant information
    teams = []
    for match in data['matches']:
        home_team = match['team1']
        away_team = match['team2']
        
        # Handle cases where the score might be missing
        if 'score' in match and 'ft' in match['score']:
            score = match['score']['ft']
            home_score, away_score = score[0], score[1]
        else:
            home_score, away_score = None, None

        teams.append({
            'team': home_team,
            'opponent': away_team,
            'home_score': home_score,
            'away_score': away_score,
            'location': 'home'
        })

        teams.append({
            'team': away_team,
            'opponent': home_team,
            'home_score': home_score,
            'away_score': away_score,
            'location': 'away'
        })

    teams_df = pd.DataFrame(teams)
    teams_df.dropna(inplace=True)
    teams_df['home_score'] = teams_df['home_score'].astype(int)
    teams_df['away_score'] = teams_df['away_score'].astype(int)
    print("Data cleaned successfully.")
    return teams_df
