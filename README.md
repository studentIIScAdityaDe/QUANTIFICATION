# QUANTIFICATION

A comprehensive Python package for data quantification, statistical analysis, and visualization. This toolkit provides easy-to-use functions for common quantification tasks, making it perfect for students, researchers, and data analysts.

## Features

- 📊 **Statistical Analysis**: Calculate mean, median, standard deviation, percentiles, and more
- 📈 **Data Visualization**: Create beautiful plots including distributions, comparisons, and correlations
- 🔍 **Data Summarization**: Generate comprehensive statistical summaries with one function call
- 🎓 **Educational**: Well-documented code with examples perfect for learning
- 🚀 **Easy to Use**: Simple API that works with lists, NumPy arrays, and Pandas Series

## Installation

1. Clone this repository:
```bash
git clone https://github.com/studentIIScAdityaDe/QUANTIFICATION.git
cd QUANTIFICATION
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Quick Start

### Basic Statistical Analysis

```python
from quantification import calculate_mean, calculate_median, calculate_std, summarize_data

# Your data
data = [85, 92, 78, 95, 88, 76, 89, 93, 84, 90]

# Calculate statistics
mean = calculate_mean(data)
median = calculate_median(data)
std = calculate_std(data)

print(f"Mean: {mean:.2f}")
print(f"Median: {median:.2f}")
print(f"Standard Deviation: {std:.2f}")

# Get complete summary
summary = summarize_data(data)
print(summary)
```

### Data Visualization

```python
from quantification import plot_distribution, plot_comparison, plot_correlation

# Plot distribution
plot_distribution(data, title="Score Distribution", bins=10)

# Compare categories
comparison_data = {'Group A': 85, 'Group B': 92, 'Group C': 78}
plot_comparison(comparison_data, title="Group Comparison")

# Correlation analysis
x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]
plot_correlation(x, y, title="X vs Y")
```

## Documentation

### Statistical Functions

#### `calculate_mean(data)`
Calculate the arithmetic mean (average) of a dataset.

**Parameters:**
- `data`: List, NumPy array, or Pandas Series

**Returns:** Float

#### `calculate_median(data)`
Calculate the median (middle value) of a dataset.

**Parameters:**
- `data`: List, NumPy array, or Pandas Series

**Returns:** Float

#### `calculate_std(data, ddof=1)`
Calculate the standard deviation of a dataset.

**Parameters:**
- `data`: List, NumPy array, or Pandas Series
- `ddof`: Delta degrees of freedom (default=1 for sample std)

**Returns:** Float

#### `calculate_percentiles(data, percentiles=[25, 50, 75])`
Calculate specified percentiles of a dataset.

**Parameters:**
- `data`: List, NumPy array, or Pandas Series
- `percentiles`: List of percentile values (0-100)

**Returns:** Dictionary mapping percentile to value

#### `summarize_data(data)`
Generate a comprehensive summary of statistical measures.

**Parameters:**
- `data`: List, NumPy array, or Pandas Series

**Returns:** Dictionary containing count, mean, std, min, 25%, 50%, 75%, max

### Visualization Functions

#### `plot_distribution(data, title, xlabel, ylabel, bins, save_path)`
Create a histogram to visualize data distribution.

**Parameters:**
- `data`: Input data
- `title`: Plot title (default: "Data Distribution")
- `xlabel`: X-axis label (default: "Value")
- `ylabel`: Y-axis label (default: "Frequency")
- `bins`: Number of histogram bins (default: 30)
- `save_path`: Optional path to save figure

#### `plot_comparison(data_dict, title, xlabel, ylabel, save_path)`
Create a bar chart to compare categories.

**Parameters:**
- `data_dict`: Dictionary with category names as keys and values
- `title`: Plot title (default: "Data Comparison")
- `xlabel`: X-axis label (default: "Category")
- `ylabel`: Y-axis label (default: "Value")
- `save_path`: Optional path to save figure

#### `plot_correlation(x_data, y_data, title, xlabel, ylabel, save_path)`
Create a scatter plot with trend line to visualize correlation.

**Parameters:**
- `x_data`: Data for x-axis
- `y_data`: Data for y-axis
- `title`: Plot title (default: "Correlation Plot")
- `xlabel`: X-axis label (default: "X Variable")
- `ylabel`: Y-axis label (default: "Y Variable")
- `save_path`: Optional path to save figure

## Examples

### Example 1: Analyzing Test Scores

```python
from quantification import calculate_mean, calculate_std, plot_distribution

test_scores = [85, 92, 78, 95, 88, 76, 89, 93, 84, 90]

mean_score = calculate_mean(test_scores)
std_score = calculate_std(test_scores)

print(f"Average Score: {mean_score:.2f} ± {std_score:.2f}")

plot_distribution(test_scores, title="Test Score Distribution", bins=5)
```

### Example 2: Comparing Groups

```python
from quantification import plot_comparison

group_averages = {
    'Control': 78.5,
    'Treatment A': 85.2,
    'Treatment B': 92.7
}

plot_comparison(group_averages, 
                title="Treatment Effect on Performance",
                ylabel="Average Score")
```

### Example 3: Studying Relationships

```python
from quantification import plot_correlation

hours_studied = [2, 3, 1, 5, 4, 2, 4, 5, 3, 4]
exam_scores = [65, 75, 60, 95, 85, 70, 80, 90, 73, 82]

plot_correlation(hours_studied, exam_scores,
                title="Study Time vs Exam Performance",
                xlabel="Hours Studied",
                ylabel="Exam Score")
```

## Running Examples

The `examples/` directory contains ready-to-run scripts:

```bash
# Run basic statistics example
python examples/basic_statistics.py

# Run visualization demo
python examples/visualization_demo.py

# Open Jupyter notebook tutorial
jupyter notebook examples/tutorial.ipynb
```

## Project Structure

```
QUANTIFICATION/
├── quantification/          # Main package directory
│   ├── __init__.py         # Package initialization
│   ├── statistics.py       # Statistical functions
│   └── visualization.py    # Visualization functions
├── examples/               # Example scripts and notebooks
│   ├── basic_statistics.py
│   ├── visualization_demo.py
│   └── tutorial.ipynb
├── requirements.txt        # Python dependencies
├── .gitignore             # Git ignore rules
└── README.md              # This file
```

## Requirements

- Python 3.7+
- NumPy >= 1.24.0
- Pandas >= 2.0.0
- Matplotlib >= 3.7.0
- SciPy >= 1.10.0
- Jupyter >= 1.0.0
- Seaborn >= 0.12.0

## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

## License

This project is open source and available for educational purposes.

## Support

For questions or support, please open an issue on the GitHub repository.

## Acknowledgments

Created to help friends and colleagues with quantification and data analysis tasks. Special thanks to the IISc community for inspiration and support!