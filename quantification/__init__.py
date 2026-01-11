"""
Quantification Utilities Package

A collection of utilities for data quantification, analysis, and visualization.
"""

__version__ = "1.0.0"
__author__ = "Your Name"

from .statistics import (
    calculate_mean,
    calculate_median,
    calculate_std,
    calculate_percentiles,
    summarize_data
)

from .visualization import (
    plot_distribution,
    plot_comparison,
    plot_correlation
)

__all__ = [
    'calculate_mean',
    'calculate_median',
    'calculate_std',
    'calculate_percentiles',
    'summarize_data',
    'plot_distribution',
    'plot_comparison',
    'plot_correlation'
]
