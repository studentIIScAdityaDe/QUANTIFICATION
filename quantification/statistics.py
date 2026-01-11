"""
Statistical Analysis Functions

This module provides common statistical functions for data quantification.
"""

import numpy as np
import pandas as pd
from typing import Union, List, Dict


def calculate_mean(data: Union[List, np.ndarray, pd.Series]) -> float:
    """
    Calculate the mean (average) of a dataset.
    
    Args:
        data: Input data as list, numpy array, or pandas Series
        
    Returns:
        Mean value as float
        
    Example:
        >>> calculate_mean([1, 2, 3, 4, 5])
        3.0
    """
    return np.mean(data)


def calculate_median(data: Union[List, np.ndarray, pd.Series]) -> float:
    """
    Calculate the median (middle value) of a dataset.
    
    Args:
        data: Input data as list, numpy array, or pandas Series
        
    Returns:
        Median value as float
        
    Example:
        >>> calculate_median([1, 2, 3, 4, 5])
        3.0
    """
    return np.median(data)


def calculate_std(data: Union[List, np.ndarray, pd.Series], ddof: int = 1) -> float:
    """
    Calculate the standard deviation of a dataset.
    
    Args:
        data: Input data as list, numpy array, or pandas Series
        ddof: Delta degrees of freedom (default=1 for sample std)
        
    Returns:
        Standard deviation as float
        
    Example:
        >>> calculate_std([1, 2, 3, 4, 5])
        1.58...
    """
    return np.std(data, ddof=ddof)


def calculate_percentiles(data: Union[List, np.ndarray, pd.Series], 
                         percentiles: List[float] = [25, 50, 75]) -> Dict[float, float]:
    """
    Calculate specified percentiles of a dataset.
    
    Args:
        data: Input data as list, numpy array, or pandas Series
        percentiles: List of percentile values to calculate (0-100)
        
    Returns:
        Dictionary mapping percentile to value
        
    Example:
        >>> calculate_percentiles([1, 2, 3, 4, 5], [25, 50, 75])
        {25: 2.0, 50: 3.0, 75: 4.0}
    """
    return {p: np.percentile(data, p) for p in percentiles}


def summarize_data(data: Union[List, np.ndarray, pd.Series]) -> Dict[str, float]:
    """
    Generate a comprehensive summary of statistical measures.
    
    Args:
        data: Input data as list, numpy array, or pandas Series
        
    Returns:
        Dictionary containing count, mean, std, min, 25%, 50%, 75%, max
        
    Example:
        >>> stats = summarize_data([1, 2, 3, 4, 5])
        >>> stats['mean']
        3.0
    """
    data_array = np.array(data)
    
    return {
        'count': len(data_array),
        'mean': np.mean(data_array),
        'std': np.std(data_array, ddof=1),
        'min': np.min(data_array),
        '25%': np.percentile(data_array, 25),
        '50%': np.percentile(data_array, 50),
        '75%': np.percentile(data_array, 75),
        'max': np.max(data_array)
    }
