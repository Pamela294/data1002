import pandas as pd
import numpy as np

# 1. Load your original dataset
df = pd.read_csv('sleep_study_1000.csv')

# 2. Shuffle the dataset randomly (use random_state for reproducibility)
shuffled_df = df.sample(frac=1, random_state=42).reset_index(drop=True)

# 3. Split into 4 equal chunks
chunks = np.array_split(shuffled_df, 4)

# 4. Save each chunk to a separate CSV file
for i, chunk in enumerate(chunks):
    chunk.to_csv(f'split_dataset_{i+1}.csv', index=False)