#  IMDB dataset and this dataset contains 50,000 movie reviews in CSV format.
# https://media.geeksforgeeks.org/wp-content/uploads/20250228115748017361/IMDB-Dataset.csv
from pathlib import Path
import pandas as pd

working_dir = Path(r"D:\CODE\DATA")
datafile = working_dir / "IMDB-Dataset.csv"

df = pd.read_csv(datafile)

print(df.head())

# Step 2: Understanding the Dataset
# The dataset contains two columns: 
# review: Contains the movie review text
# sentiment: It shows whether the review is positive or negative
