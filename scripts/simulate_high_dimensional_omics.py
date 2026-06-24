# simulate_high_dimensional_omics.py
# Purpose: Simulate a high-dimensional omics-style dataset for benchmarking

import numpy as np
import pandas as pd
from pathlib import Path

# Set random seed for reproducibility
np.random.seed(123)

# Define dataset dimensions
n_samples = 60
n_features = 500

# Simulate two biological groups
groups = np.array(["Control"] * 30 + ["Treatment"] * 30)

# Simulate high-dimensional omics-style data
X = np.random.normal(loc=0, scale=1, size=(n_samples, n_features))

# Add a small group-associated signal to the first 20 features
X[groups == "Treatment", 0:20] += 0.8

# Create feature names and sample IDs
feature_names = [f"feature_{i+1}" for i in range(n_features)]
sample_ids = [f"S{i+1:03d}" for i in range(n_samples)]

# Create dataframe
omics_data = pd.DataFrame(X, columns=feature_names)
omics_data.insert(0, "sample_id", sample_ids)
omics_data.insert(1, "group", groups)

# Create output folder
Path("data").mkdir(exist_ok=True)

# Save simulated dataset
omics_data.to_csv("data/simulated_high_dimensional_omics.csv", index=False)

print("Simulated omics dataset saved to data/simulated_high_dimensional_omics.csv")
print(f"Number of samples: {n_samples}")
print(f"Number of features: {n_features}")
print("Group-associated signal added to features 1–20.")
