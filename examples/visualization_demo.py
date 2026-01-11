"""
Example: Data Visualization

This script demonstrates how to use the quantification package for data visualization.
"""

import sys
from pathlib import Path

# Add parent directory to path to import quantification module
sys.path.insert(0, str(Path(__file__).parent.parent))

from quantification import plot_distribution, plot_comparison, plot_correlation
import numpy as np


def main():
    print("=" * 60)
    print("DATA VISUALIZATION EXAMPLES")
    print("=" * 60)
    
    # Example 1: Distribution plot
    print("\nGenerating distribution plot...")
    data = np.random.normal(100, 15, 1000)
    plot_distribution(data, 
                     title="Normal Distribution (μ=100, σ=15)",
                     xlabel="Value",
                     ylabel="Frequency")
    
    # Example 2: Comparison plot
    print("\nGenerating comparison plot...")
    comparison_data = {
        'Group A': 85.5,
        'Group B': 92.3,
        'Group C': 78.9,
        'Group D': 88.7,
        'Group E': 95.2
    }
    plot_comparison(comparison_data,
                   title="Performance Comparison Across Groups",
                   xlabel="Group",
                   ylabel="Average Score")
    
    # Example 3: Correlation plot
    print("\nGenerating correlation plot...")
    x = np.linspace(0, 10, 50)
    y = 2 * x + 3 + np.random.normal(0, 2, 50)
    plot_correlation(x, y,
                    title="Linear Relationship Example",
                    xlabel="Independent Variable (X)",
                    ylabel="Dependent Variable (Y)")
    
    print("\n" + "=" * 60)
    print("All visualizations generated successfully!")


if __name__ == "__main__":
    main()
