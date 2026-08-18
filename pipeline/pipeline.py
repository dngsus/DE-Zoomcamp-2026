# import os
# output_dir = "outputs"
# os.makedirs(output_dir, exist_ok=True)

import sys
print("arguments", sys.argv)

month = int(sys.argv[1])
print(f"Running pipeline for month {month}")

import pandas as pd

df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
print(df.head())

#df.to_parquet(f"{output_dir}/output_month{sys.argv[1]}.parquet")

df.to_parquet(f"output_month_{sys.argv[1]}.parquet")