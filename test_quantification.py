"""
Simple tests for the quantification package.

These tests verify that all the main functions work correctly.
"""

import sys
sys.path.insert(0, '.')

import numpy as np
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend for testing

from quantification import (
    calculate_mean,
    calculate_median,
    calculate_std,
    calculate_percentiles,
    summarize_data,
    plot_distribution,
    plot_comparison,
    plot_correlation
)


def test_statistics():
    """Test statistical functions."""
    print("Testing statistical functions...")
    
    data = [1, 2, 3, 4, 5]
    
    # Test mean
    mean = calculate_mean(data)
    assert mean == 3.0, f"Expected mean 3.0, got {mean}"
    print("  ✓ calculate_mean works")
    
    # Test median
    median = calculate_median(data)
    assert median == 3.0, f"Expected median 3.0, got {median}"
    print("  ✓ calculate_median works")
    
    # Test std
    std = calculate_std(data)
    assert abs(std - 1.5811388300841898) < 0.0001, f"Expected std ~1.581, got {std}"
    print("  ✓ calculate_std works")
    
    # Test percentiles
    percentiles = calculate_percentiles(data, [25, 50, 75])
    assert 25 in percentiles and 50 in percentiles and 75 in percentiles
    print("  ✓ calculate_percentiles works")
    
    # Test summarize_data
    summary = summarize_data(data)
    assert 'count' in summary and 'mean' in summary and 'std' in summary
    assert summary['count'] == 5
    assert summary['mean'] == 3.0
    print("  ✓ summarize_data works")
    
    print("All statistical tests passed! ✓\n")


def test_visualization():
    """Test visualization functions."""
    print("Testing visualization functions...")
    
    # Test plot_distribution
    data = np.random.normal(100, 15, 100)
    try:
        plot_distribution(data, title="Test Distribution")
        print("  ✓ plot_distribution works")
    except Exception as e:
        print(f"  ✗ plot_distribution failed: {e}")
        raise
    
    # Test plot_comparison
    comparison_data = {'A': 10, 'B': 20, 'C': 15}
    try:
        plot_comparison(comparison_data, title="Test Comparison")
        print("  ✓ plot_comparison works")
    except Exception as e:
        print(f"  ✗ plot_comparison failed: {e}")
        raise
    
    # Test plot_correlation
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([2, 4, 6, 8, 10])
    try:
        plot_correlation(x, y, title="Test Correlation")
        print("  ✓ plot_correlation works")
    except Exception as e:
        print(f"  ✗ plot_correlation failed: {e}")
        raise
    
    print("All visualization tests passed! ✓\n")


def test_with_different_input_types():
    """Test that functions work with different input types."""
    print("Testing with different input types...")
    
    # Python list
    list_data = [1, 2, 3, 4, 5]
    assert calculate_mean(list_data) == 3.0
    print("  ✓ Works with Python lists")
    
    # NumPy array
    array_data = np.array([1, 2, 3, 4, 5])
    assert calculate_mean(array_data) == 3.0
    print("  ✓ Works with NumPy arrays")
    
    # Pandas Series
    import pandas as pd
    series_data = pd.Series([1, 2, 3, 4, 5])
    assert calculate_mean(series_data) == 3.0
    print("  ✓ Works with Pandas Series")
    
    print("All input type tests passed! ✓\n")


def main():
    """Run all tests."""
    print("=" * 60)
    print("QUANTIFICATION PACKAGE TESTS")
    print("=" * 60)
    print()
    
    try:
        test_statistics()
        test_visualization()
        test_with_different_input_types()
        
        print("=" * 60)
        print("ALL TESTS PASSED! ✓")
        print("=" * 60)
        return 0
    except Exception as e:
        print("\n" + "=" * 60)
        print(f"TEST FAILED: {e}")
        print("=" * 60)
        return 1


if __name__ == "__main__":
    exit(main())
