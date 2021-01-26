import requests
import os 
import pandas as pd

download_url = "https://raw.githubusercontent.com/fivethirtyeight/data/master/nba-elo/nbaallelo.csv"

outDir = r'D:\CODE\PYSCRIPTS\PY_DATA'
target_csv_path = os.path.join(outDir,"nba_all_elo.csv")

# Download nba results in csv
# response = requests.get(download_url)
# response.raise_for_status()    # Check that the request was successful
# with open(target_csv_path, "wb") as f:
#     f.write(response.content)

# Reading csv file using pandas function read_csv
nba = pd.read_csv(target_csv_path)

# Calculate Length of Data using len function => 126314
len(nba)

# Dimensionality or shape results in a tuple containing the number of rows and columns.
# (126314, 23)
nba.shape

# Check First 5 rows using head() function
nba.head()

# Set Display to all columns using set_option function in pandas
pd.set_option("display.max.columns", None)

# Set Precision to 2 i.e. 
pd.set_option("display.precision", 2)

# Last 5 rows
nba.tail()

# Data Frame column data types
nba.info()

# overview of values each column contains
nba.describe()

import numpy as np
# .describe only analyzes numeric columns by default, but you can provide other data types with include parameter:
nba.describe(include=np.object)

    