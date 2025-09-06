# Swedish Survey Data Analysis

Interactive data visualization of Swedish regional survey data across 5 regions: Blekinge nordöstra Skåne, Kalmar Kronoberg, Malmö, Nordvästra Skåne, and Södra Skåne.

## Launch in Binder

Click the badge below to launch this notebook in an interactive environment:

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/pnetto/survey-notebooks/main?labpath=regions.ipynb)

> **Note**: Replace `USERNAME/REPOSITORY` in the badge URL above with your actual GitHub username and repository name.

## What's in this notebook?

This interactive notebook allows you to:

- **Visualize regional trends** across different survey indicators
- **Compare regions** side by side over time
- **Interactive year range selection** to focus on specific time periods
- **5-year span analysis** for broader trend analysis

## Features

### Interactive Visualizations
- Dropdown menus to select different survey indicators
- Year range sliders to focus on specific time periods
- Line plots comparing all 5 regions simultaneously

### Data Processing
- Automated cleaning and standardization of Excel survey data
- Handling of Swedish characters (ä, å, ö)
- Time series aggregation and grouping

## Running Locally

If you want to run this locally, you'll need:

```bash
pip install -r requirements.txt
```

Then open `regions.ipynb` in Jupyter Lab or Jupyter Notebook.

## Data Sources

The analysis uses survey data from 5 Swedish regions:
- Blekinge nordöstra Skåne
- Kalmar Kronoberg 
- Malmö
- Nordvästra Skåne
- Södra Skåne

Each dataset contains various indicators tracked over multiple years, including metrics related to outdoor environment, substance abuse, disturbances, crime exposure, safety concerns, and public trust.
