import pandas as pd

outDir = r'D:\CODE\PYSCRIPTS\PY_DATA'
target_csv_path = os.path.join(outDir,"nba_all_elo.csv")

nba = pd.read_csv(target_csv_path)

# Examine how often specific values occur in a column
nba["team_id"].value_counts()

nba["fran_id"].value_counts()

# It seems that a team named "Lakers" played 6024 games, 
# but only 5078 of those were played by the Los Angeles Lakers. 
# Find out who the other "Lakers" team is:
nba.loc[nba["fran_id"] == "Lakers", "team_id"].value_counts()
# LAL    5078
# MNL     946

# Minneapolis Lakers ("MNL") played 946 games. Find out when they played those games:
nba.loc[nba["team_id"] == "MNL", "date_game"].min()
# '1/1/1949'

nba.loc[nba["team_id"] == "MNL", "date_game"].max()
# '4/9/1959'

nba.loc[nba["team_id"] == "MNL", "date_game"].agg(("min", "max"))
# min    1/1/1949
# max    4/9/1959

