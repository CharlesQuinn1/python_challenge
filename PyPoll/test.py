import pandas as pd
from pathlib import Path


file = Path("PyPoll/Resources/election_data.csv")
file_df = pd.read_csv(file)

file_df