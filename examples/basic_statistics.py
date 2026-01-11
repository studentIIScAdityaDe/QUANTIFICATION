"""
Example: Basic Statistical Analysis

This script demonstrates how to use the quantification package for basic statistical analysis.
"""

import sys
from pathlib import Path

# Add parent directory to path to import quantification module
sys.path.insert(0, str(Path(__file__).parent.parent))

from quantification import (
    calculate_mean,
    calculate_median,
    calculate_std,
    calculate_percentiles,
    summarize_data
)
import numpy as np


def main():
    # Generate sample data
    print("=" * 60)
    print("BASIC STATISTICAL ANALYSIS EXAMPLE")
    print("=" * 60)
    
    # Example 1: Analyzing test scores
    test_scores = [85, 92, 78, 95, 88, 76, 89, 93, 84, 90]
    print("\nExample 1: Test Scores Analysis")
    print(f"Test Scores: {test_scores}")
    print(f"Mean: {calculate_mean(test_scores):.2f}")
    print(f"Median: {calculate_median(test_scores):.2f}")
    print(f"Standard Deviation: {calculate_std(test_scores):.2f}")
    
    percentiles = calculate_percentiles(test_scores, [25, 50, 75])
    print(f"Percentiles: {percentiles}")
    
    # Example 2: Complete summary
    print("\n" + "-" * 60)
    print("Example 2: Complete Statistical Summary")
    summary = summarize_data(test_scores)
    for key, value in summary.items():
        print(f"{key:>10s}: {value:.2f}")
    
    # Example 3: Random data analysis
    print("\n" + "-" * 60)
    print("Example 3: Random Data Analysis")
    random_data = np.random.normal(100, 15, 1000)
    print(f"Analyzing {len(random_data)} random samples from Normal(100, 15)")
    
    summary = summarize_data(random_data)
    for key, value in summary.items():
        print(f"{key:>10s}: {value:.2f}")
    
    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()
