# How to Run the Benchmarking Workflow

## Overview

This document explains how to run the example quantum-inspired omics benchmarking workflow.

The current workflow uses simulated high-dimensional omics-style data and classical baseline methods. It is intended as an exploratory and reproducible starting point for future quantum-inspired omics method development.

## Required software

- Python 3.9 or higher
- Git, optional for local version control
- Jupyter Notebook, optional for future notebook-based extensions

## Required Python packages

Install the required packages using:

```bash
pip install numpy pandas scikit-learn matplotlib
python scripts/simulate_high_dimensional_omics.py
python scripts/classical_pca_benchmark.py
python scripts/kernel_model_benchmark.py
data/
results/
figures/
data/simulated_high_dimensional_omics.csv
results/classical_pca_scores.csv
results/classical_pca_explained_variance.csv
results/kernel_model_benchmark_summary.csv
results/kernel_model_classification_report.csv
results/kernel_model_confusion_matrix.csv
figures/classical_pca_benchmark.png
