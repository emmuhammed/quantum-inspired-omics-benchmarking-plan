# classical_pca_benchmark.py
# Purpose: Apply PCA to simulated high-dimensional omics data as a classical baseline

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Load simulated omics data
data = pd.read_csv("data/simulated_high_dimensional_omics.csv")

# Separate metadata and features
metadata = data[["sample_id", "group"]]
X = data.drop(columns=["sample_id", "group"])

# Standardise features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Run PCA
pca = PCA(n_components=2)
pca_scores = pca.fit_transform(X_scaled)

# Create PCA results dataframe
pca_results = pd.DataFrame({
    "sample_id": metadata["sample_id"],
    "group": metadata["group"],
    "PC1": pca_scores[:, 0],
    "PC2": pca_scores[:, 1]
})

# Create output folders
Path("results").mkdir(exist_ok=True)
Path("figures").mkdir(exist_ok=True)

# Save PCA scores
pca_results.to_csv("results/classical_pca_scores.csv", index=False)

# Save explained variance
explained_variance = pd.DataFrame({
    "component": ["PC1", "PC2"],
    "explained_variance_ratio": pca.explained_variance_ratio_
})

explained_variance.to_csv("results/classical_pca_explained_variance.csv", index=False)

# Plot PCA
plt.figure(figsize=(6, 4))

for group in pca_results["group"].unique():
    subset = pca_results[pca_results["group"] == group]
    plt.scatter(subset["PC1"], subset["PC2"], label=group)

plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title("Classical PCA baseline for simulated omics data")
plt.legend()
plt.tight_layout()

plt.savefig("figures/classical_pca_benchmark.png", dpi=300)
plt.close()

print("PCA benchmark complete.")
print("Outputs saved in results/ and figures/.")
