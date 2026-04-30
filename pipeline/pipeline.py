import sys

import pandas as pd

df = pd.DataFrame({"day": [1, 2], "num_passengers": [3, 4]})
month = int(sys.argv[1])

df['month'] = month

print(df.head())

df.to_parquet(f"output_day_{sys.argv[1]}.parquet")

print("arguments", sys.argv)
