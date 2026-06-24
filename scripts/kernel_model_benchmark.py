# kernel_model_benchmark.py
# Purpose: Benchmark a classical kernel-based classifier on simulated high-dimensional omics data

import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load simulated omics data
data = pd.read_csv("data/simulated_high_dimensional_omics.csv")

# Separate features and labels
X = data.drop(columns=["sample_id", "group"])
y = data["group"]

# Split into training and testing datasets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.30,
    random_state=123,
    stratify=y
)

# Build a kernel-based model pipeline
kernel_model = Pipeline([
    ("scaler", StandardScaler()),
    ("svm_rbf", SVC(kernel="rbf", C=1.0, gamma="scale"))
])

# Fit model
kernel_model.fit(X_train, y_train)

# Predict test set
y_pred = kernel_model.predict(X_test)

# Evaluate model
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred, output_dict=True)
conf_matrix = confusion_matrix(y_test, y_pred)

# Cross-validation accuracy
cv_scores = cross_val_score(kernel_model, X, y, cv=5)

# Create output folder
Path("results").mkdir(exist_ok=True)

# Save summary results
summary = pd.DataFrame({
    "metric": ["test_accuracy", "mean_cv_accuracy", "sd_cv_accuracy"],
    "value": [accuracy, cv_scores.mean(), cv_scores.std()]
})

summary.to_csv("results/kernel_model_benchmark_summary.csv", index=False)

# Save classification report
report_df = pd.DataFrame(report).transpose()
report_df.to_csv("results/kernel_model_classification_report.csv")

# Save confusion matrix
conf_matrix_df = pd.DataFrame(
    conf_matrix,
    index=["Actual_Control", "Actual_Treatment"],
    columns=["Predicted_Control", "Predicted_Treatment"]
)

conf_matrix_df.to_csv("results/kernel_model_confusion_matrix.csv")

print("Kernel model benchmark complete.")
print(f"Test accuracy: {accuracy:.3f}")
print(f"Mean cross-validation accuracy: {cv_scores.mean():.3f}")
print("Outputs saved in results/.")
