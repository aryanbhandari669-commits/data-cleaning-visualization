# Data Cleaning & Visualization Project

A comprehensive Python project for cleaning, processing, and visualizing datasets with interactive dashboards.

## Features

- **Data Cleaning**: Handle missing values, duplicates, and outliers
- **Preprocessing**: Normalize and standardize data
- **Visualizations**: Generate interactive dashboards using Plotly
- **Statistical Analysis**: Compute descriptive statistics and correlations
- **Automated Reports**: Create HTML-based visual reports

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Generate Sample Data

```bash
python sample_data_generator.py
```

### Run Data Cleaning & Visualization

```bash
python main.py
```

## Project Structure

- `data_cleaning.py` - Data preprocessing and cleaning utilities
- `visualization.py` - Interactive dashboard generation
- `main.py` - Main execution script
- `sample_data_generator.py` - Generate sample dataset
- `requirements.txt` - Project dependencies

## Output

- `cleaned_data.csv` - Processed dataset
- `dashboards/` - Interactive HTML reports:
  - `missing_data_heatmap.html`
  - `distributions.html`
  - `correlation_heatmap.html`
  - `statistical_summary.html`
  - `boxplots.html`
  - `scatter_plots.html`
  - `value_counts.html`

## Capabilities

### Data Cleaning
- Missing value imputation (mean/median/mode)
- Duplicate row removal
- Outlier detection and handling (IQR method)
- Data validation

### Visualization
- Distribution analysis
- Correlation analysis
- Statistical summaries
- Box plots
- Scatter plot matrices
- Value frequency charts
- Missing data heatmaps
