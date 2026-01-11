"""
Visualization Functions

This module provides functions for creating visualizations of quantitative data.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Union, List, Optional


def plot_distribution(data: Union[List, np.ndarray, pd.Series], 
                     title: str = "Data Distribution",
                     xlabel: str = "Value",
                     ylabel: str = "Frequency",
                     bins: int = 30,
                     save_path: Optional[str] = None) -> None:
    """
    Create a histogram to visualize the distribution of data.
    
    Args:
        data: Input data as list, numpy array, or pandas Series
        title: Title for the plot
        xlabel: Label for x-axis
        ylabel: Label for y-axis
        bins: Number of bins for histogram
        save_path: Optional path to save the figure
        
    Example:
        >>> plot_distribution([1, 2, 2, 3, 3, 3, 4, 4, 5], title="Sample Data")
    """
    plt.figure(figsize=(10, 6))
    plt.hist(data, bins=bins, edgecolor='black', alpha=0.7)
    plt.title(title, fontsize=14, fontweight='bold')
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    plt.grid(True, alpha=0.3)
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    plt.show()


def plot_comparison(data_dict: dict,
                   title: str = "Data Comparison",
                   xlabel: str = "Category",
                   ylabel: str = "Value",
                   save_path: Optional[str] = None) -> None:
    """
    Create a bar chart to compare different categories of data.
    
    Args:
        data_dict: Dictionary where keys are category names and values are measurements
        title: Title for the plot
        xlabel: Label for x-axis
        ylabel: Label for y-axis
        save_path: Optional path to save the figure
        
    Example:
        >>> plot_comparison({'A': 10, 'B': 20, 'C': 15}, title="Category Comparison")
    """
    plt.figure(figsize=(10, 6))
    categories = list(data_dict.keys())
    values = list(data_dict.values())
    
    plt.bar(categories, values, edgecolor='black', alpha=0.7)
    plt.title(title, fontsize=14, fontweight='bold')
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    plt.grid(True, alpha=0.3, axis='y')
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    plt.show()


def plot_correlation(x_data: Union[List, np.ndarray, pd.Series],
                    y_data: Union[List, np.ndarray, pd.Series],
                    title: str = "Correlation Plot",
                    xlabel: str = "X Variable",
                    ylabel: str = "Y Variable",
                    save_path: Optional[str] = None) -> None:
    """
    Create a scatter plot to visualize correlation between two variables.
    
    Args:
        x_data: Data for x-axis
        y_data: Data for y-axis
        title: Title for the plot
        xlabel: Label for x-axis
        ylabel: Label for y-axis
        save_path: Optional path to save the figure
        
    Example:
        >>> plot_correlation([1, 2, 3, 4, 5], [2, 4, 6, 8, 10], title="X vs Y")
    """
    plt.figure(figsize=(10, 6))
    plt.scatter(x_data, y_data, alpha=0.6, s=50)
    
    # Add trend line
    z = np.polyfit(x_data, y_data, 1)
    p = np.poly1d(z)
    plt.plot(x_data, p(x_data), "r--", alpha=0.8, linewidth=2, label='Trend line')
    
    # Calculate correlation coefficient
    correlation = np.corrcoef(x_data, y_data)[0, 1]
    plt.text(0.05, 0.95, f'r = {correlation:.3f}', 
             transform=plt.gca().transAxes, 
             fontsize=12, verticalalignment='top',
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    plt.title(title, fontsize=14, fontweight='bold')
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.legend()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    plt.show()
