import pandas as pd
import numpy as np

df = pd.read_csv('sleep_health_dataset.csv')

shuffled_df = df.sample(frac=1, random_state=42).reset_index(drop=True)

chunks = np.array_split(shuffled_df, 4)

for i, chunk in enumerate(chunks):
    chunk.to_csv(f'split_dataset_{i+1}.csv', index=False)